#!/usr/bin/env python
#    Copyright 2013 Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import setuptools
import sys


requirements = [
    'netaddr>=0.7.5',
    'PyYAML>=3.10',
    'netifaces>=0.5',
    'urwid>=1.1.1',
    'requests>=2.5.2,!=2.8.0,!=2.9.0',
]

if sys.version_info[0:2] == (2, 6):
    requirements.append('OrderedDict>=1.1')

setuptools.setup(
    name="fuelmenu",
    version='10.0.0',
    description="Console util for pre-configuration of Fuel server",
    author="Matthew Mosesohn",
    author_email="mmosesohn@mirantis.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Console :: Curses",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Topic :: Security",
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: Proxy Servers",
        "Topic :: Software Development :: Testing"
    ],
    install_requires=requirements,
    include_package_data=True,
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'fuelmenu = fuelmenu.fuelmenu:main',
        ],
    },
)
