import os
from setuptools import setup

setup(
    author = 'Alexandre Gobbo',
    description = 'Read EDF files',
    py_modules = ['EdfFile'],
    name = 'edffile',
    install_requires = ('numpy'),
    license="MIT",
    version = os.environ['PKG_VERSION'],
)
