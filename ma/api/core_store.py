import logging

import ma.api.base_class

_LOGGER = logging.getLogger(__name__)


class CoreStoreApi(ma.api.base_class.Api):
    def get_list(self):
        l = self.magento.core_store.list()
        return l
