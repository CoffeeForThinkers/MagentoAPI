import logging
import collections

import ma.api.base_class
import ma.entities.product
import ma.utility

_LOGGER = logging.getLogger()


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

    def create_product(self, product_type, attribute_set_id, sku, 
                       catalog_product_create_entity):
        cpce_dict = \
            ma.utility.get_dict_from_named_tuple(
                catalog_product_create_entity)

        product_id = \
            self.magento.catalog_product.create(
                product_type, 
                attribute_set_id, 
                sku, 
                cpce_dict)

        product_id = int(product_id)

        _LOGGER.info("Created product with ID (%d).", product_id)

        return product_id
