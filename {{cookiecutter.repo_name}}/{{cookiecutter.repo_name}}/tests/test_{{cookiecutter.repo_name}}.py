#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unit tests for the `{{ cookiecutter.repo_name }}` module."""

import unittest

from {{ cookiecutter.repo_name }} import {{ cookiecutter.repo_name }}


class Test{{ cookiecutter.repo_name|capitalize }}(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
