#!/usr/bin/env python
'''
Created on Aug 25, 2016

@author: Thomas Adriaan Hellinger
'''
from setuptools import setup

setup(name='Woordje',
      version='0.0.1',
      description='A web-based text editor for creating quick and small blog posts. Like little poops of wisdom and/or happiness.',
      author='Thomas Adriaan Hellinger',
      author_email='thellinger@acm.org',
      url='https://github.com/brotherjack/woordje',
      packages=["woordje"],
      package_dir={'woordje': 'woordje',
                   'root': 'woordje/root'},
      package_data={'woordje': 
                    ['templates/*.html',
                     'static/css/*.css',
                     'static/fonts/*',
                     'static/js/*.js',
                     'static/images/*.png'
                     ]},
        entry_points={
            'console_scripts': [
                'woordje = woordje.app:main',
      ],
  },
)
