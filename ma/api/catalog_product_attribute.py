import logging

import ma.api.base_class

_LOGGER = logging.getLogger()


class CatalogProductAttributeApi(ma.api.base_class.Api):
    def get_list(self, attribute_set_id):
        l = self.magento.catalog_product_attribute.list(attribute_set_id)
        return l
