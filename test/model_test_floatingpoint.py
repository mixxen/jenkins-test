"""
model_test_floatingpoint.py

Unit tests to demonstrate FloatingPointError for model.

AlgorithmHub. All rights reserved.
https://www.algorithmhub.com/
"""

import unittest
import error_funcs


class TestFloatingPoint(unittest.TestCase):
    def setUp(self):
        pass

    def test_floating_point(self):
        """
        Function to test where the passed value passes
        the FloatingPoint error.

        Try with the following functions:
        zero_division_error(-4.): will return assertion error
        zero_division_error(4.): will not return any error
        """

        try:
            error_funcs.floating_point_error(-4.)
        except FloatingPointError:
            self.fail(
                "The floating point value passed has some problems"
            )


if __name__ == '__main__':
    unittest.main()
