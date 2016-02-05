#!/usr/bin/env python3 -u
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup


with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup(
    name='projecteuler',
    version='1.0',
    author='Frederick Wagner',
    url='https://github.com/doctaphred/projecteuler',
    description='Solutions to selected Project Euler problems',
    packages=find_packages(exclude=['tests']),
    entry_points={
        'console_scripts': [
            'euler = projecteuler.__main__:main',
            ],
        },
    install_requires=requirements,
    )
