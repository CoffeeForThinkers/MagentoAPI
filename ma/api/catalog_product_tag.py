import logging

import ma.api.base_class

_LOGGER = logging.getLogger(__name__)


class CatalogProductTagApi(ma.api.base_class.Api):
    def get_list(self, product_id):
        l = self.magento.catalog_product_tag.list(product_id)
        return l
