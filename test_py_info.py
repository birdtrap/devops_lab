#!/usr/bin/env python
"""python info test"""

from unittest import TestCase

import py_info

class TestPrime(TestCase):

   def setUp(self):
       """Init"""

   def test_get_inst_pack(self):
       """test for get_inst_pack return"""
       self.assertTrue(py_info.get_inst_pack())

   def test_py_info_dict(self):
       """test for py_info_dict"""
       self.assertTrue(type(py_info.py_info_dict()) is dict)

   def tearDown(self):
       """finish"""

