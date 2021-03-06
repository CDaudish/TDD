import unittest
import random
from check_pwd import check_pwd


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertFalse(check_pwd(""))

    def test2(self):
        self.assertFalse(check_pwd("h"))

    def test3(self):
        self.assertTrue(check_pwd("12345678"))

    def test4(self):
        self.assertTrue(check_pwd("12345678901234"))

    def test5(self):
        self.assertTrue(check_pwd("12345678901234567890"))

    def test6(self):
        self.assertFalse(check_pwd("123456789012345678900"))

    def test7(self):
        self.assertTrue(check_pwd("123456789012"))



        
