#!/usr/bin/env python2.7

import os.path
import setuptools

import ma

_APP_PATH = os.path.dirname(ma.__file__)

with open(os.path.join(_APP_PATH, 'resources', 'README.rst')) as f:
      _LONG_DESCRIPTION = f.read()

with open(os.path.join(_APP_PATH, 'resources', 'requirements.txt')) as f:
      _INSTALL_REQUIRES = list(map(lambda s: s.strip(), f))

setuptools.setup(
    name='magento_adapter',
    version=ma.__version__,
    description="Magento API interfaces",
    long_description=_LONG_DESCRIPTION,
    classifiers=[],
    keywords='',
    author='Dustin Oprea',
    author_email='dustin@randomingenuity.com',
    url='https://github.com/CoffeeForThinkers/MagentoAPI',
    license='GPL3',
    packages=setuptools.find_packages(exclude=['dev']),
    include_package_data=True,
    zip_safe=False,
    install_requires=_INSTALL_REQUIRES,
    package_data={
        'ma': [
            'resources/README.rst',
            'resources/requirements.txt',
        ],
    },
    scripts=[
        'ma/resources/scripts/ma_help',
        'ma/resources/scripts/ma_truncate_products',
    ],
)
