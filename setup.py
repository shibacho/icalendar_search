#!/usr/bin/env python
# Copyright (C) 2011 by fantakeshi 
# Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php
# Author: fantakeshi
# Contact: fantakeshi1@gmail.com

from distutils.core import setup

setup(name='icalendar_search',
      version='0.1',
      author='fantakeshi',
      author_email='fantakeshi1@gmail.com',
      description='iCalendar search module',
      license='MIT',
      url='https://github.com/fantakeshi/icalendar_search',
      package_dir = {'icalendar_search':'src/icalendar_search'},
      packages=['icalendar_search']
      )