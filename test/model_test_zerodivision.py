"""
model_test_zerodivision.py

Unit tests to demonstrate ZeroDivisionError for model.

AlgorithmHub. All rights reserved.
https://www.algorithmhub.com/
"""

import unittest
import error_funcs
import sys


class TestZeroDivision(unittest.TestCase):
    def setUp(self):
        pass

    def test_zero_division(self):
        """
        Function to test where the passed value passes
        the ZeroDivision error.

        Try with the following functions:
        zero_division_error(5, 0): will return assertion error
        zero_division_error(5, 2): will not return any error
        """

        try:
            error_funcs.zero_division_error(5, 0)
        except ZeroDivisionError:
            self.fail(
                "The denominator cannot be ZERO"
            )


if __name__ == '__main__':
    print sys.argv
    unittest.main()
