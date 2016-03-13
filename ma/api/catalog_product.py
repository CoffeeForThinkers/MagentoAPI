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

        records = self.magento.catalog_product.list(filters)
        for record in records:
            record['product_id'] = int(record['product_id'])
            yield record

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
            self, attribute_set_id, sku, catalog_product_create_entity):
        """
        Logic based on:

        http://netzkollektiv.com/blog/add-configurable-products-via-soapxml-rpc
        """

        cpce_dict = \
            ma.utility.get_dict_from_named_tuple(
                catalog_product_create_entity)

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

    def assign_simple_product_to_configurable_product(
            self, configurable_product_id, simple_sku_list, attribute_codes, 
            attribute_labels, pricing_list):
        """`attribute_codes`: A list of attribute codes to group configuration on.
        
        `attributes_labels`: A dictionary of labels for the attribute codes.
        
        `pricing` is a dictionary keyed by all of the values for all of the 
        attributes that we're grouping by. Yes, there will be collisions if any 
        observed values between any of the grouped attributes happen to match.
        """

        _LOGGER.debug("Assigning simple products to configurable with ID "
                      "(%d): %s", configurable_product_id, simple_sku_list)

        arguments = [
            configurable_product_id,
            simple_sku_list,
            attribute_codes,
            attribute_labels,
            pricing_list,
        ]

        (c, sid) = self.soap2
        c.catalogProductTypeConfigurableAssign(*([sid] + arguments))

    def list_of_additional_attributes(self, product_type, attribute_set_id):
        rows = self.magento.catalog_product.listOfAdditionalAttributes(
                product_type, 
                attribute_set_id)

        return { int(r['attribute_id']): r for r in rows }
