import os
import sys

from setuptools import setup
from setuptools import find_packages

version = __import__('configbuilder').VERSION

base_path = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(base_path, 'README.rst'), 'r') as f:
    description = f.read()

setup(
    name='configbuilder',
    version=version,
    packages=find_packages(),
    license='BSD',
)
