#!/usr/bin/env python

import os
import sys

from setuptools import setup


PYTHON_CURRENT = sys.version_info[0]
PYTHON_REQUIRED = 3

if PYTHON_CURRENT < PYTHON_REQUIRED:
    sys.stderr.write("Python >= 3 is required.")
    sys.exit(1)


setup(
    name='indextools',
    version='1.0.0',
    description='indextools - bijective mapping between semantic value and index.',
    author='Andrea Baisero',
    author_email='andrea.baisero@gmail.com',
    url='https://github.com/bigblindbais/indextools',

    packages=['indextools'],
    package_dir={'':'src'},
    test_suite='tests',

    install_requires=['numpy'],
    license='MIT',
)
