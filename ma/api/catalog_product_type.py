import logging

import ma.api.base_class

_LOGGER = logging.getLogger(__name__)


class CatalogProductTypeApi(ma.api.base_class.Api):
    def get_list(self):
        l = self.magento.catalog_product_type.list()
        return l
