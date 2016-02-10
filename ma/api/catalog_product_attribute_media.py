import logging

import ma.api.base_class

_LOGGER = logging.getLogger()


class CatalogProductAttributeMediaApi(ma.api.base_class.Api):
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
