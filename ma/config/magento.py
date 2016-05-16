import os
import logging

_LOGGER = logging.getLogger(__name__)

SCHEME = os.environ.get('MAGENTO_SCHEME', 'https')
USERNAME = os.environ['MAGENTO_USERNAME']
PASSWORD = os.environ['MAGENTO_PASSWORD']
HOSTNAME = os.environ['MAGENTO_HOSTNAME']
PORT = int(os.environ.get('MAGENTO_PORT', '443'))

_LOGGER.debug("CONFIG: S=[%s] U=[%s] P=[%s] H=[%s] P=(%d)",
              SCHEME, USERNAME, PASSWORD, HOSTNAME, PORT)
