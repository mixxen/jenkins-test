"""
model_test_invalidvalue.py

Unit tests to demonstrate InvalidValueError for model.

AlgorithmHub. All rights reserved.
https://www.algorithmhub.com/
"""

import unittest
import error_funcs


class TestInvalidValue(unittest.TestCase):
    def setUp(self):
        pass

    def test_invalid_value(self):
        """
        Function to test where the passed value passes
        the InvalidValue error.

        Try with the following functions:
        invalid_value_error(1, 2, None): will return assertion error
        invalid_value_error(1, 2, 3): will not return any error
        """

        try:
            error_funcs.invalid_value_error(1, 2, 3)
        except Exception:
            self.fail(
                "Cannot have None values"
            )


if __name__ == '__main__':
    unittest.main()
