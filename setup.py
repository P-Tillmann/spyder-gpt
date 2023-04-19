# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2023, Peter Tillmann
#
# Licensed under the terms of the MIT license
# ----------------------------------------------------------------------------
"""
GPT in Spyder setup.
"""
from setuptools import find_packages
from setuptools import setup

from spyder_gpt import __version__


setup(
    # See: https://setuptools.readthedocs.io/en/latest/setuptools.html
    name="spyder-gpt",
    version=__version__,
    author="Peter Tillmann",
    author_email="Peter.tillmann@mail.de",
    description="A simple GPT interface in Spyder",
    license="MIT license",
    url="https://github.com/p-tillmann/spyder-gpt",
    python_requires='>= 3.7',
    install_requires=[
        "qtpy",
        "qtawesome",
        "spyder>=5.0.1",
    ],
    packages=find_packages(),
    entry_points={
        "spyder.plugins": [
            "spyder_gpt = spyder_gpt.spyder.plugin:GPTinSpyder"
        ],
    },
    classifiers=[
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering",
    ],
)
