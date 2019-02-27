#!/usr/bin/env python
# coding=utf-8

from distutils.core import setup

version = '0.2a'

setup(
    name='jefferson',
    version=version,
    description='Jefferson: jffs2 fs tool',
    author='Stefan Viehböck',
    url='https://github.com/svidovich/jefferson-3',
    license='MIT',
    maintainer='Samuel Vidovich sam@finitestate.io',
    requires=['cstruct'],
    packages=['jefferson'],
    package_dir={'jefferson': 'src/jefferson'},
    scripts=['src/scripts/jefferson'],
)
