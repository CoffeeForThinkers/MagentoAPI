import logging

import ma.api.base_class

_LOGGER = logging.getLogger(__name__)


class AttributeSetApi(ma.api.base_class.Api):
    def get_list(self):
        l = self.magento.catalog_product_attribute_set.list()
        for record in l:
            record['set_id'] = int(record['set_id'])

            yield record
