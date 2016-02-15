import os
import logging

import magento

import ma.config.magento

_TIMESTAMP_FORMAT = '%Y-%m-%d %H:%M:%S'

_LOGGER = logging.getLogger(__name__)


class _ApiResources(object):
    def __init__(self):
        self.__ar = self.__get_api_resource()

    def __get_server_config(self):
        scheme = ma.config.magento.SCHEME
        username = ma.config.magento.USERNAME
        password = ma.config.magento.PASSWORD
        hostname = ma.config.magento.HOSTNAME
        port = ma.config.magento.PORT

        return {
            'scheme': scheme,
            'username': username,
            'password': password,
            'hostname': hostname,
            'port': port,
        }

    def __get_api_resource(self):
        c = self.__get_server_config()

        m = magento.MagentoAPI(
                c['hostname'], 
                c['port'], 
                c['username'], 
                c['password'],
                proto=c['scheme'])

        return m

    @property
    def api_resource(self):
        return self.__ar


_API_RESOURCES = None
def _get_api_resources():
    global _API_RESOURCES
    if _API_RESOURCES is None:
        _API_RESOURCES = _ApiResources()

    return _API_RESOURCES


class Api(object):
    def __init__(self):
        ars = _get_api_resources()
        self.__ar = ars.api_resource

    @property
    def magento(self):
        return self.__ar
