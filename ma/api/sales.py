import logging

import ma.api.constants
import ma.api.base_class

_LOGGER = logging.getLogger()


class SalesApi(ma.api.base_class.Api):
    def get_transactions(self, from_timestamp, to_timestamp):
        format = ma.api.constants.TIMESTAMP_FORMAT_1

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

        # We don't want to distill the results because we don't want to 
        # interfere with the data at this layer. We'll leave it as an exercise 
        # for the receiver of this data.

        return l
