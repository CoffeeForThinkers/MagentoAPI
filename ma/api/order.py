import logging

import ma.constants
import ma.api.base_class

_LOGGER = logging.getLogger(__name__)


class OrderApi(ma.api.base_class.Api):
    def get_transactions(self, from_timestamp, to_timestamp):
        format = ma.constants.TIMESTAMP_FORMAT_1

        from_timestamp_phrase = from_timestamp.strftime(format)
        to_timestamp_phrase = to_timestamp.strftime(format)

        _LOGGER.debug("Returning transactions from [%s] to [%s].", 
                      from_timestamp_phrase, to_timestamp_phrase)

        filters = {
            'created_at': {
                'from': from_timestamp_phrase,
                'to': to_timestamp_phrase,
            }, 
        }

        l = self.magento.sales_order_invoice.list(filters)
        return l
