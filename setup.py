#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
from shpinfo import __version__

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with io.open('README.rst') as f:
    readme = f.read()

with io.open('HISTORY.rst') as f:
    history = f.read().replace('.. :changelog:', '')

with io.open('requirements.txt', encoding='utf-8') as f:
    requirements = f.read().splitlines()

setup(
    name='shpinfo',
    version=__version__,
    description='A command line program to print meta information about the given shapefile.',
    long_description=readme + '\n\n' + history,
    author='Ramiro Gómez',
    author_email='code@ramiro.org',
    url='https://github.com/yaph/shpinfo',
    packages=[
        'shpinfo',
    ],
    package_dir={'shpinfo':
                 'shpinfo'},
    include_package_data=True,
    install_requires=requirements,
    license='MIT',
    zip_safe=False,
    keywords='gis geospatial geography shapefile',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    entry_points={
        'console_scripts': [
            'shpinfo = shpinfo.shpinfo:main'
        ]
    }
)