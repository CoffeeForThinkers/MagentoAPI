import os
import logging

import magento

import ma.config.magento

_TIMESTAMP_FORMAT = '%Y-%m-%d %H:%M:%S'

_LOGGER = logging.getLogger(__name__)


class Api(object):
    def __init__(self):
        self.__m = self.__get_resource()

    def __get_server_config(self):
        username = ma.config.magento.USERNAME
        password = ma.config.magento.PASSWORD
        hostname = ma.config.magento.HOSTNAME
        port = ma.config.magento.PORT

        return {
            'username': username,
            'password': password,
            'hostname': hostname,
            'port': port,
        }

    def __get_resource(self):
        c = self.__get_server_config()
        m = magento.MagentoAPI(
                c['hostname'], 
                c['port'], 
                c['username'], 
                c['password'])

        return m

    @property
    def magento(self):
        return self.__m
