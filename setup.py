#!/usr/bin/env python3

import setuptools

with open("README.md","r") as fh:
  longdescription = fh.read()

setuptools.setup(name='cetem_publico',
    version='0.0.7',
    description='Python WRAPPER For CETEM Publico Corpus',
    author='André Santos',
    author_email='afs@inesctec.pt',
    packages = setuptools.find_packages(),
    long_description = longdescription,
    url='https://github.com/andrefs/cetem_publico',
    project_urls={
        'Bug Reports': 'https://github.com/andrefs/cetem_publico/issues',
        'Source': 'https://github.com/andrefs/cetem_publico/',
    },
)
