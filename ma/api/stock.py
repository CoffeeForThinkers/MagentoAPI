import logging

import ma.api.base_class

_LOGGER = logging.getLogger(__name__)


class StockApi(ma.api.base_class.Api):
    def get_list_with_ids(self, product_ids, do_allow_missing=False):
        assert product_ids, "Please a nonempty list of product-IDs."

        l = self.magento.cataloginventory_stock_item.list(product_ids)

        assert \
            do_allow_missing is True or len(l) == len(product_ids), \
            "One or more inventory products doesn't exist."

        return l

    def get_list_with_skus(self, product_skus, do_allow_missing=False):
        assert product_skus, "Please a nonempty list of product-SKUs."

# NOTE(dustin): This is currently the same request as _id(), but we want to
#               keep the calls separate just in case Magento finally gets their 
#               act together.
        l = self.magento.cataloginventory_stock_item.list(product_skus)

        assert \
            do_allow_missing is True or len(l) == len(product_skus), \
            "One or more inventory products doesn't exist."

        return l
