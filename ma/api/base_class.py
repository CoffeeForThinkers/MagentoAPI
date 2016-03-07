import os
import logging
import functools

import magento
import SOAPpy

import ma.config.magento

_TIMESTAMP_FORMAT = '%Y-%m-%d %H:%M:%S'

_LOGGER = logging.getLogger(__name__)


class _ApiResources(object):
    def __init__(self):
        self.__c = self.__get_server_config()

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

    def __get_rpc_resource(self):
        _LOGGER.info("XML-RPC HOSTNAME=[%s]", self.__c['hostname'])

        m = magento.MagentoAPI(
                self.__c['hostname'], 
                self.__c['port'], 
                self.__c['username'], 
                self.__c['password'],
                proto=self.__c['scheme'])

        return m

    def __get_soap1_resource(self):
        url_template = '%(scheme)s://%(hostname)s/index.php/api/soap/?wsdl'
        url = url_template % self.__c

        _LOGGER.info("SOAP1 URL: %s", url)

        client = SOAPpy.WSDL.Proxy(url)
        session = client.login(self.__c['username'], self.__c['password'])

        return (client, session)

    def __get_soap2_resource(self):
        url_template = '%(scheme)s://%(hostname)s/index.php/api/v2_soap/?wsdl'
        url = url_template % self.__c

        _LOGGER.info("SOAP2 URL: %s", url)

        client = SOAPpy.WSDL.Proxy(url)
        
#        arguments = {
#            'username': self.__c['username'],
#            'apiKey': self.__c['password'],
#        }

#        arguments = [
#            self.__c['username'],
#            self.__c['password'],
#        ]

#        session = client.login(arguments)

        # SOAP 2
        session_id = client.login(self.__c['username'], self.__c['password'])

        return (client, session_id)

    @property
    def rpc_resource(self):
        try:
            return self.__rr
        except AttributeError:
            self.__rr = self.__get_rpc_resource()
            return self.__rr

    @property
    def soap1_resource(self):
        try:
            return self.__sr1
        except AttributeError:
            self.__sr1 = self.__get_soap1_resource()
            return self.__sr1

    @property
    def soap2_resource(self):
        try:
            return self.__sr2
        except AttributeError:
            self.__sr2 = self.__get_soap2_resource()
            return self.__sr2


_API_RESOURCES = None
def _get_api_resources():
    global _API_RESOURCES
    if _API_RESOURCES is None:
        _API_RESOURCES = _ApiResources()

    return _API_RESOURCES


class Api(object):
    def __init__(self):
        self.__ars = _get_api_resources()

# TODO(dustin): We'd like to rename this, but it'd be a breaking-change.
    @property
    def magento(self):
        try:
            return self.__rr
        except AttributeError:
            self.__rr = self.__ars.rpc_resource
            return self.__rr

    @property
    def soap1(self):
        try:
            sr1 = self.__sr1
        except AttributeError:
            self.__sr1 = self.__ars.soap1_resource
            sr1 = self.__sr1

#        return functools.partial(self.__sr[0].call, self.__sr[1])
        return sr1

    @property
    def soap2(self):
        try:
            sr2 = self.__sr2
        except AttributeError:
            self.__sr2 = self.__ars.soap2_resource
            sr2 = self.__sr2

#        return functools.partial(self.__sr[0].call, self.__sr[1])
        return sr2
