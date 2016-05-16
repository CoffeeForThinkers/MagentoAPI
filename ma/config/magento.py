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

# Hash used to execute remote re-indexing and cache refresh.
UTILITY_HASH = os.environ.get('MAGENTO_UTILITY_HASH', None)

# Magento Cache Types
MAGENTO_CACHE_TYPES = {
    'config': 'System(config.xml, local.xml) and modules configuration files(config.xml).',
    'layout_general_cache_tag': 'Layout building instructions.',
    'block_html': 'Page blocks HTML.',
    'translate': 'Translation files.',
    'collection_data': 'Collection data files.',
    'eav': 'Entity types declaration cache.',
    'config_api': 'Web Services definition files (api.xml).',
    'config_api2': 'Web Services definition files (api2.xml).',
    'aitsys': 'Extended class-rewriting subsystem.',
}

# Magento Index Types
MAGENTO_INDEX_TYPES = {
    '1': 'Product Attributes',
    '2': 'Product Prices.',
    '3': 'Catalog URL Rewrites',
    '4': 'Product Flat Data',
    '5': 'Category Flat Data',
    '6': 'Category Products',
    '7': 'Catalog Search index',
    '8': 'Stock Status',
    '9': 'Tag Aggregation Data',
    '12': 'Layered Navigation by aheadWorks',
}

# Magento Maintenance URLs
_domain = SCHEME + '://' + HOSTNAME
MAGENTO_MAINTENANCE_URL = {
    'cache': _domain + '/utility/cache/refresh/type/{0}/{1}',
    'index': _domain + '/utility/reindex/index/process/{0}/{1}'
}
