#!/usr/bin/env python
# -*- coding: utf-8 -*-

from io import open
import os
import sys

from setuptools import setup

import {{ cookiecutter.repo_name }}


def open_file(filename):
    """Open and read the file *filename*."""
    with open(filename) as f:
        return f.read()


readme = open_file('README.rst')
history = open_file('HISTORY.rst').replace('.. :changelog:', '')

setup(
    name='{{ cookiecutter.repo_name }}',
    version={{ cookiecutter.repo_name }}.__version__,
    description='{{ cookiecutter.project_short_description }}',
    long_description=readme + '\n\n' + history,
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    packages=[
        '{{ cookiecutter.repo_name }}',
    ],
    package_dir={'{{ cookiecutter.repo_name }}': '{{ cookiecutter.repo_name }}'},
    include_package_data=True,
    install_requires=[
    ],
    license='BSD',
    keywords='{{ cookiecutter.repo_name }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
)
