import logging
import hashlib
import base64
import os.path

logging.getLogger('requests').setLevel(logging.WARNING)
import requests

import ma.config.general
import ma.entities.product
import ma.api.base_class
import ma.utility

_LOGGER = logging.getLogger(__name__)


class ImageAcquisitionFailError(Exception):
    pass


class MediaApi(ma.api.base_class.Api):
    def __init__(self, image_url_template=None, *args, **kwargs):
        self.__image_url_template = image_url_template

        super(MediaApi, self).__init__(*args, **kwargs)

    def get_list_with_product_id(self, product_id):
        l = self.magento.catalog_product_attribute_media.list(product_id)

        # Example return:
        #
        #[
        #    {
        #        "exclude": "0",
        #        "file": "/m/s/msj003t_1.jpg",
        #        "label": "",
        #        "position": "1",
        #        "types": [
        #            "image",
        #            "small_image",
        #            "thumbnail"
        #        ],
        #        "url": "http://dev.bugatchi.com/media/catalog/product/m/s/msj003t_1.jpg"
        #    },
        #    {
        #        "exclude": "0",
        #        "file": "/m/s/msj003a_1.jpg",
        #        "label": "",
        #        "position": "2",
        #        "types": [],
        #        "url": "http://dev.bugatchi.com/media/catalog/product/m/s/msj003a_1.jpg"
        #    },
        #]

        return l

    def get_list_with_product_sku(self, product_sku):
# NOTE(dustin): This is currently the same request as _id(), but we want to
#               keep the calls separate just in case Magento finally gets their
#               act together.
        l = self.magento.catalog_product_attribute_media.list(product_sku)
        return l

    def __get_image_data(self, image_filepath, is_relative=True):
        """Acquire the image data. Accomodate both local and remote requests.
        """

        if is_relative is True and self.__image_url_template is not None:
            replacements = {
                'rel_filepath': image_filepath,
            }
            url = self.__image_url_template % replacements
        else:
            url = image_filepath

        local_uri_prefix = 'file://'
        len_ = len(local_uri_prefix)
        if url[:len_].lower() == local_uri_prefix:
            filepath = url[len_:]
            path = os.path.dirname(filepath)
            assert \
                os.path.exists(path) is True, \
                "Local image download path does not exist: " + path

#            _LOGGER.info("Reading image [%s] from local: [%s]", image_filepath, filepath)

            try:
                with open(filepath, 'rb') as f:
                    data = f.read()
            except IOError:
                data = None

            if data is None:
                raise ImageAcquisitionFailError("Could not copy image: [{0}]".format(filepath))
        else:
#            _LOGGER.info("Downloading product image [%s]: [%s]", image_filepath, url)

            r = requests.get(url=url, stream=True)

            try:
                r.raise_for_status()
            except requests.exceptions.HTTPError as e:
                r = None

            if r is None:
                raise ImageAcquisitionFailError("Could not download image: [{0}]".format(url))

            data = r.raw.read()

        return data

    def __build_image_entity(self, image_filepath, is_relative=True):
        image_data = self.__get_image_data(image_filepath, is_relative)
        pivot = image_filepath.rfind('.')
        extension = image_filepath[pivot + 1:].lower()
        mime_type = \
            ma.config.general.FILE_EXTENSION_TO_MIMETYPE_MAPPING[extension]

        # We translate what might potentially be file-paths into an opaque
        # string.
        filename = hashlib.sha1(image_filepath).hexdigest()
        image_data_encoded = base64.b64encode(image_data)

        cpife = \
            ma.entities.product.build_catalog_product_image_file_entity(
                    content=image_data_encoded,
                    mime=mime_type,
                    name=filename,
                )

        return cpife

    def create(self, product_id, image_filepath, label_text, for_types,
               position=0, is_relative=True):
        """This "create" call also supports removing and, apparently, multiple
        files of different types, but the parameters are in conflict with each
        other and generally don't make sense. We can add different methods for
        additional use-cases later.
        """

        _LOGGER.info("Uploading image [%s] for product with ID [%d].",
                     image_filepath, product_id)

        cpife = self.__build_image_entity(image_filepath, is_relative)
        cpife_dict = ma.utility.get_dict_from_named_tuple(cpife)

        do_exclude = False
        do_remove = False

        cpamce = \
            ma.entities.product.build_catalog_product_attribute_media_create_entity(
                    file=cpife_dict,
                    label=label_text,
                    position=str(position),
                    types=for_types,
                    exclude=str(int(do_exclude)),
                    remove=str(int(do_remove))
                )

        cpamce_dict = ma.utility.get_dict_from_named_tuple(cpamce)

        upload_rel_filepath = \
            self.magento.catalog_product_attribute_media.create(
                product_id,
                cpamce_dict)

        return upload_rel_filepath

    def update(self, product_id, image_filepath, mage_file_path, label_text=None, for_types=None,
               position=0, is_relative=True):

        _LOGGER.info("Media Update: Uploading image [%s] for product with ID [%d].",
                     image_filepath, product_id)

        cpife = self.__build_image_entity(image_filepath, is_relative)
        cpife_dict = ma.utility.get_dict_from_named_tuple(cpife)

        do_exclude = False
        do_remove = False

        cpamce = \
            ma.entities.product.build_catalog_product_attribute_media_create_entity(
                    file=cpife_dict,
                    label=label_text,
                    position=str(position),
                    types=for_types,
                    exclude=str(int(do_exclude)),
                    remove=str(int(do_remove))
                )

        cpamce_dict = ma.utility.get_dict_from_named_tuple(cpamce)

        is_updated = \
            self.magento.catalog_product_attribute_media.update(
                product_id,
                mage_file_path,
                cpamce_dict)

        return is_updated

    def remove_with_sku(self, sku, rel_filepath):
        return self.magento.catalog_product_attribute_media.remove(sku, rel_filepath, 'sku')

    def remove_with_id(self, product_id, rel_filepath):
        return self.magento.catalog_product_attribute_media.remove(product_id, rel_filepath)
