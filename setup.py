from setuptools import setup, find_packages
import sys
import os

version = '0.1'

setup(name='ecdsa_keygen',
      version=version,
      description="Simple ECDSA key pair generation cli tool",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Sean Sanders',
      author_email='sean.d.sanders@gmail.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
          'ecdsa',
      ]
)