import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 0 +")
        self.assertEqual(1, result)
    def test_subtract(self):
        result = rpn.calculate('5 0 -')
        self.assertEqual(5, result)
    def test_exponentiation(self):
        result = rpn.calculate("1 1 ^")
        self.assertEqual(1, result)
