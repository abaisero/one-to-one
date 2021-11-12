#!/usr/bin/env python

import sys

from setuptools import setup

if sys.version_info < (3, 7):
    sys.stderr.write('Python >= 3.7 is required.')
    sys.exit(1)


with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read()


setup(
    name='one-to-one',
    version='0.1.0',
    description='one-to-one - bijective mapping between semantic value and index.',
    author='Andrea Baisero',
    author_email='andrea.baisero@gmail.com',
    url='https://github.com/bigblindbais/one-to-one',
    packages=['one_to_one'],
    package_dir={'': 'src'},
    install_requires=requirements,
    test_suite='tests',
    license='MIT',
)
