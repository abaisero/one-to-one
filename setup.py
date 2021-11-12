#!/usr/bin/env python

import sys

from setuptools import setup

if sys.version_info < (3, 7):
    sys.stderr.write('Python >= 3.7 is required.')
    sys.exit(1)


setup(
    name='one-to-one',
    version='0.1.0',
    description='one-to-one - bijective mapping between semantic value and index.',
    author='Andrea Baisero',
    author_email='andrea.baisero@gmail.com',
    url='https://github.com/bigblindbais/one-to-one',
    packages=['one_to_one'],
    package_dir={'': 'src'},
    test_suite='tests',
    license='MIT',
)
