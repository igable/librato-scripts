#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    try:
        from ez_setup import use_setuptools
        use_setuptools()
        from setuptools import setup, find_packages
    except ImportError :
        from distutils import setup

setup(name="librato-scripts",
      version="0.1",
      url="https://github.com/igable/librato-python-scripts",
      description="Simple utilities for sending data to Librato Metrics",
      author="Ian Gable",
      author_email="igable@uvic.ca",
      scripts=['librato-imap'],
      install_requires=[
       "librato>=0.1"],
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        ],
)
