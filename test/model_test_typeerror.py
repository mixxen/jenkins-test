"""
model_test_typeerror.py

Unit tests to demonstrate TypeError for model.

AlgorithmHub. All rights reserved.
https://www.algorithmhub.com/
"""

import unittest
import error_funcs


class TestType(unittest.TestCase):
    def setUp(self):
        pass

    def test_type(self):
        """
        Function to test where the passed value passes
        the TypeError.

        Try with the following functions:
        type_error(-1, 2, '3'): will return assertion error
        type_error(1, 2, 3): will not return any error
        """

        try:
            error_funcs.type_error(1, 2, '3')
        except TypeError:
            self.fail(
                "Cannot have multiple data types"
            )


if __name__ == '__main__':
    unittest.main()
