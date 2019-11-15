#!/usr/bin/env python3

import setuptools

with open("README.rst","rt") as fh:
  longdescription = fh.read()

setuptools.setup(name='cetem-publico',
    version='0.0.14',
    description='Python wrapper for the CETEMPublico corpus',
    author='André Santos',
    author_email='afs@inesctec.pt',
    packages = setuptools.find_packages(),
    long_description = longdescription,
    long_description_content_type = 'text/x-rst',
    url='https://github.com/andrefs/cetem_publico',
    install_requires=['clint'],
    project_urls={
        'Bug Reports': 'https://github.com/andrefs/cetem_publico/issues',
        'Source': 'https://github.com/andrefs/cetem_publico/',
    },
)
