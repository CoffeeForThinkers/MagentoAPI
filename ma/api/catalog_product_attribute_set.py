import logging

import ma.api.base_class

_LOGGER = logging.getLogger()


class CatalogProductAttributeSetApi(ma.api.base_class.Api):
    def get_list(self):
        l = self.magento.catalog_product_attribute_set.list()
        return l
