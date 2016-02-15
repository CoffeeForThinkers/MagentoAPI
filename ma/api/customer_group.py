import logging

import ma.api.base_class

_LOGGER = logging.getLogger()


class CustomerGroupApi(ma.api.base_class.Api):
    def get_list(self):
        l = self.magento.customer_group.list()

        for record in l:
            record['customer_group_id'] = int(record['customer_group_id'])
            yield record
