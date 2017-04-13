"""
model_test_valueerror.py

Unit tests to demonstrate ValueError for model.

AlgorithmHub. All rights reserved.
https://www.algorithmhub.com/
"""

import unittest
import error_funcs


class TestType(unittest.TestCase):
    def setUp(self):
        pass

    def test_value(self):
        """
        Function to test where the passed value passes
        the ValueError.

        Try with the following functions:
        value_error(256): will return assertion error
        value_error(97): will not return any error
        """

        try:
            error_funcs.value_error(256)
        except ValueError:
            self.fail(
                "Must pass value within range (256)"
            )


if __name__ == '__main__':
    unittest.main()
