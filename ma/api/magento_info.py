import logging

import ma.api.base_class

_LOGGER = logging.getLogger(__name__)


class MagentoInfoApi(ma.api.base_class.Api):
    def get_info(self):
        l = self.magento.core_magento.info()
        return l
