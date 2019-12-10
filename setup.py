#!/usr/bin/env python

from distutils.core import setup

setup(name='hmtoinflux',
      version='0.0',
      description='a bridge for sensor data from homematic to influxdb',
      long_description=open('README.md').read(),
      author='David Bauer',
      author_email='hmtoinflux@debauer.net',
      packages=['hmtoinflux'],
     )