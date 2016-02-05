#!/usr/bin/env python3 -u
# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name='projecteuler',
    version='1.0',
    author='Frederick Wagner',
    url='https://github.com/doctaphred/projecteuler',
    description='Solutions to selected Project Euler problems',
    packages=['projecteuler'],
    entry_points={
        'console_scripts': [
            'euler = projecteuler.__main__:main',
            ],
        },
    )
