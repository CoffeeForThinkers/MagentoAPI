import os
import logging

_LOGGER = logging.getLogger(__name__)

USERNAME = os.environ['MAGENTO_USERNAME']
PASSWORD = os.environ['MAGENTO_PASSWORD']
HOSTNAME = os.environ['MAGENTO_HOSTNAME']
PORT = int(os.environ.get('MAGENTO_PORT', '80'))

_LOGGER.debug("CONFIG: U=[%s] P=[%s] H=[%s] P=(%d)",
              username, password, hostname, port)
