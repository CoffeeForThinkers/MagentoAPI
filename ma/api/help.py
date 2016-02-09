import logging

import ma.api.base_class

_LOGGER = logging.getLogger()


class HelpApi(ma.api.base_class.Api):
    def print_help(self):
        self.magento.help()
