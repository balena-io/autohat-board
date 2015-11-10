#!/usr/bin/env python

import re
from setuptools import setup, find_packages

setup(
    version="0.0.1",
    name="sd-mux-ctrl",
    description="Command line tool for SD card switch controller",
    author="Adam Malinowski",
    author_email="a.malinowsk2@partner.samsung.com",
    packages=["sd-mux-ctrl"],
    license='Apache-2.0',
)
