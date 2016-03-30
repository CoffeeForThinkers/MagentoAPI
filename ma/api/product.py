import logging
import collections

import ma.api.base_class
import ma.entities.product
import ma.utility

_LOGGER = logging.getLogger(__name__)


class ProductApi(ma.api.base_class.Api):
    def get_info_with_id(self, product_id):
        i = self.magento.catalog_product.info(product_id)

        return i

    def get_info_with_sku(self, product_sku):

# NOTE(dustin): This is currently the same request as _id(), but we want to
#               keep the calls separate just in case Magento finally gets their 
#               act together.
        i = self.magento.catalog_product.info(product_sku)

        return i

    def get_list(self, categories=[]):
        filters = {}

# TODO(dustin): We can't get this to work right and Magento isn't cooperating 
#               with our debugging effort.
        assert not categories, "A category filter is not currently supported."

#        if categories:
#            filters['category_id'] = { 'eq': '10' }#in': ','.join([str(c) for c in categories]) }

        records = self.magento.catalog_product.list(filters)
        for record in records:
            record['product_id'] = int(record['product_id'])
            yield record

    def __inject_attributes(self, cpce_dict, attributes):
        aa = { 
            'single_data': [],
            'multi_data': [],
        }

        for k, v in attributes.items():
            if issubclass(v.__class__, list) is True:
                parent_name = 'multi_data'
                v = ','.join([str(atom) for atom in v])
            else:
                parent_name = 'single_data'

            aa[parent_name].append({ 'key': k, 'value': v })

        cpce_dict['additional_attributes'] = aa

    def create_simple_product_with_sku(
            self, attribute_set_id, sku, catalog_product_create_entity, 
            attributes={}):
        cpce_dict = \
            ma.utility.get_dict_from_named_tuple(
                catalog_product_create_entity)

        self.__inject_attributes(cpce_dict, attributes)

        # We need to use SOAP2 for this call. XML-RPC (and probably SOAP1) will 
        # ignore them.

        arguments = [
            'simple', 
            str(attribute_set_id), 
            sku, 
            cpce_dict,
        ]

        (c, sid) = self.soap2
        product_id = c.catalogProductCreate(*([sid] + arguments))

        _LOGGER.info("Created SIMPLE product with ID (%d).", product_id)

        return product_id

    def update_simple_product_with_sku(
            self, sku, catalog_product_create_entity, attributes={}):
        cpce_dict = \
            ma.utility.get_dict_from_named_tuple(
                catalog_product_create_entity)

        self.__inject_attributes(cpce_dict, attributes)

        # We need to use SOAP2 for this call. XML-RPC (and probably SOAP1) will 
        # ignore them.

        arguments = [
            sku, 
            cpce_dict,
            '',
            'sku',
        ]

        (c, sid) = self.soap2
        was_updated = c.catalogProductUpdate(*([sid] + arguments))

    def create_configurable_product_with_sku(
            self, attribute_set_id, sku, catalog_product_create_entity, 
            attributes={}):
        cpce_dict = \
            ma.utility.get_dict_from_named_tuple(
                catalog_product_create_entity)

        self.__inject_attributes(cpce_dict, attributes)

        arguments = [
            'configurable', 
            str(attribute_set_id), 
            sku, 
            cpce_dict,
        ]

        (c, sid) = self.soap2
        product_id = c.catalogProductCreate(*([sid] + arguments))

        _LOGGER.info("Created CONFIGURABLE product with ID (%d).", product_id)

        return product_id

    def update_configurable_product_with_sku(
            self, sku, catalog_product_create_entity, attributes):
        cpce_dict = \
            ma.utility.get_dict_from_named_tuple(
                catalog_product_create_entity)

        self.__inject_attributes(cpce_dict, attributes)

        arguments = [
            sku, 
            cpce_dict,
            '',
            'sku',
        ]

        (c, sid) = self.soap2
        was_updated = c.catalogProductUpdate(*([sid] + arguments))

        _LOGGER.info("Updated CONFIGURABLE product with [%s]? [%s]", sku, was_updated)

    def list_of_additional_attributes(self, product_type, attribute_set_id):
        rows = self.magento.catalog_product.listOfAdditionalAttributes(
                product_type, 
                attribute_set_id)

        return { int(r['attribute_id']): r for r in rows }

    def delete_with_sku(self, sku):
        was_deleted = \
            self.magento.catalog_product.delete(sku, 'sku')

        return was_deleted

    def get_tag_list_with_id(self, product_id):
        l = self.magento.catalog_product_tag.list(product_id)
        return l

    def get_type_list(self):
        l = self.magento.catalog_product_type.list()
        return l
