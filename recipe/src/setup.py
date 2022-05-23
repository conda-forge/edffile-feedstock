from setuptools import setup

setup(
    author = 'Alexandre Gobbo',
    description = 'Read EDF files',
    py_modules = ['EdfFile'],
    name = 'edffile',
    install_requires = ('numpy'),
    license="MIT",
    version = '5.0.0',
)
