#!/usr/bin/env python
import os
from setuptools import setup
with open('textteaser/requirements.txt') as f:
    required = f.read().splitlines()
tt = 'textteaser'
setup(name='textteaser',
      version='1.0',
      description='Python Port of TextTeaser',
      url='https://github.com/datateaser/textteaser',
      author='DataTeaser',
      author_email='info@datateaser.com',
      install_requires=required,      
      packages=[tt],
      package_dir={tt:tt},
      package_data={tt:['trainer/*']},
      classifiers=[
         'Development Status :: 5 - Production',
         'Intended Audience :: Developers',
         'Programming Language :: Python :: 2',
         'Programming Language :: Python :: 3',
         'Topic :: Software Development',
         'Topic :: Software Development :: Libraries',
         'Topic :: Software Development :: Libraries :: Python Modules',
         'Topic :: Text Processing :: General'
      ],
     )
