import logging
import collections

import ma.api.base_class
import ma.entities.product
import ma.utility

_LOGGER = logging.getLogger(__name__)


class CatalogProductApi(ma.api.base_class.Api):
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

        l = self.magento.catalog_product.list(filters)
        return l

    def create_simple_product(
            self, attribute_set_id, sku, catalog_product_create_entity, 
            attributes={}):
        cpce_dict = \
            ma.utility.get_dict_from_named_tuple(
                catalog_product_create_entity)

        # Inject attributes.

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

    def create_configurable_product(
            self, attribute_set_id, sku, name, short_description, 
            website_id_list, description=None, price=0.00):
        """
        Logic based on:

        http://netzkollektiv.com/blog/add-configurable-products-via-soapxml-rpc
        """

        if description is None:
            description = short_description

        cpce_dict = {
            'name': name,
            'description': description,
            'short_description': short_description,
            'websites': website_id_list,
            'price': price,
        }

        product_id = \
            self.magento.catalog_product.create(
                'configurable', 
                attribute_set_id, 
                sku, 
                cpce_dict)

        product_id = int(product_id)

        _LOGGER.info("Created CONFIGURABLE product with ID (%d).", product_id)

        return product_id

    def list_of_additional_attributes(self, product_type, attribute_set_id):
        rows = self.magento.catalog_product.listOfAdditionalAttributes(
                product_type, 
                attribute_set_id)

        return { int(r['attribute_id']): r for r in rows }
