import logging

import ma.api.base_class

_LOGGER = logging.getLogger(__name__)


class HelpApi(ma.api.base_class.Api):
    def print_help(self):
        self.magento.help()
