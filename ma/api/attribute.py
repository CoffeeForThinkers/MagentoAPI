import logging

import ma.api.base_class

_LOGGER = logging.getLogger(__name__)


class AttributeApi(ma.api.base_class.Api):
    def get_list(self, attribute_set_id):
        rows = self.magento.catalog_product_attribute.list(attribute_set_id)
        return rows

    def get_info(self, attribute_id):
        row = self.magento.catalog_product_attribute.info(attribute_id)
        return row

    def get_options(self, attribute_id):
        rows = self.magento.catalog_product_attribute.options(attribute_id)
# TODO(dustin): If each row's value is always an integer, convert it.
        return rows
