import logging
import requests

import ma.utility
import ma.exceptions
import ma.api.base_class
import ma.config.maintenance

_LOGGER = logging.getLogger(__name__)


class MaintenanceApi(ma.api.base_class.Api):
    def __init__(self):
        self.__mst = ma.config.maintenance.MAGENTO_SECURITY_TOKEN
        if self.__mst is None:
            raise ma.exceptions.MissingSecurityTokenError("Maintenance")

        self.__mmu = ma.config.maintenance.MAGENTO_MAINTENANCE_URL
        self.__mct =  ma.config.maintenance.MAGENTO_CACHE_TYPES
        self.__mit = ma.config.maintenance.MAGENTO_INDEX_TYPES

    def __get_matching_entries(self, d, l):
        """ Returns all the dictionary entries as a tuple
            based on the matching keys from the passed list
        """

        # defaults to all entries when nothing to match.
        # Used as flag to process the entire set.
        if l is None:
            return d.items()

        return  ma.utility.match_dict_keys_from_list(d, l)

    def refresh_cache(self, cache_types=None):
        entries = self.__get_matching_entries(
                    self.__mct,
                    cache_types)

        for (k, desc) in entries:
            url =  self.__mmu['cache'].format(k, self.__mst)
            r = requests.get(url)

            if r.status_code == requests.codes.ok:
                _LOGGER.info("Cache Refresh [%s]: %s", k, desc)
            else:
                _LOGGER.warning("Unable to refresh cache: [%s]", k)

    def reindex(self, index_types=None):
        entries = self.__get_matching_entries(
                    self.__mit,
                    index_types)

        for (k, desc) in entries:
            url =  self.__mmu['index'].format(k, self.__mst)
            r = requests.get(url)

            if r.status_code == requests.codes.ok:
                _LOGGER.info("Re-index [%s]: %s", k, desc)
            else:
                _LOGGER.warning("Unable to reindex: [%s]", desc)
