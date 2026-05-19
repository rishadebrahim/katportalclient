#!/usr/bin/env python
# Copyright (c) 2015 National Research Foundation (South African Radio Astronomy Observatory)
# BSD license - see LICENSE for details

from os import path
from setuptools import setup, find_packages

this_directory = path.abspath(path.dirname(__file__))

files = {'Readme': 'README.md', 'Changelog': 'CHANGELOG.md'}

long_description = ""
for name, filename in files.items():
    if name != 'Readme':
        long_description += "# {}\n".format(name)
    with open(path.join(this_directory, filename), encoding='utf8') as _f:
        file_contents = _f.read()
    long_description += file_contents + "\n\n"

setup(
    name="katportalclient",
    description="A client for katportal.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="MeerKAT CAM Team",
    author_email="cam@ska.ac.za",
    packages=find_packages(),
    include_package_data=True,
    scripts=[],
    url='https://github.com/ska-sa/katportalclient',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Astronomy"
    ],
    platforms=["OS Independent"],
    keywords="meerkat kat ska",
    python_requires=">=3.8,<4",
    setup_requires=["katversion"],
    use_katversion=True,
    install_requires=[
        "httpx>=0.28,<1.0",
        "tornado>=6,<7",
        "websockets>=13.1,<14",
        "ujson==4.3.0",
    ],
    zip_safe=False,
)
