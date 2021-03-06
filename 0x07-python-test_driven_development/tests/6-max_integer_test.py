#!/usr/bin/python3
""" tests for max_integer function"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_normal(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = max_integer(array)
        self.assertAlmostEqual(result, 10)

    def test_notint(self):
        """Not Intes"""
        array = ["a", "b", 9]
        self.assertRaises(TypeError, max_integer, array)

    def test_numberempty(self):
        """Empty list: should return None"""
        array = []
        result = max_integer(array)
        self.assertEqual(result, None)

    def test_numbernegative(self):
        """Negative values"""
        array = [-8, -9, -3]
        result = max_integer(array)
        self.assertEqual(result, -3)

    def test_numberfloat(self):
        """Ints and floats"""
        array = [1, 2.7, 3]
        result = max_integer(array)
        self.assertEqual(result, 3)

    def test_onenumber(self):
        """One number"""
        array = [7]
        result = max_integer(array)
        self.assertEqual(result, 7)

    def test_identical(self):
        """Identical values"""
        array = [1, 1, 1, 1, 1]
        result = max_integer(array)
        self.assertEqual(result, 1)

    def test_strings(self):
        """list of strings: return the first string"""
        array = ["I", "like"]
        result = max_integer(array)
        self.assertEqual(result, "like")

    def test_none(self):
        """None as parameter:"""
        self.assertRaises(TypeError, max_integer, None)

if __name__ == '__main__':
    unittest.main()
