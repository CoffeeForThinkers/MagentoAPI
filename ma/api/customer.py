import logging

import ma.api.base_class

_LOGGER = logging.getLogger(__name__)


class CustomerApi(ma.api.base_class.Api):
    def get_group_list(self):
        l = self.magento.customer_group.list()

        for record in l:
            record['customer_group_id'] = int(record['customer_group_id'])
            yield record
