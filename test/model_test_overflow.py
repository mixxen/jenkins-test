"""
model_test_overflow.py

Unit tests to demonstrate OverflowError for model.

AlgorithmHub. All rights reserved.
https://www.algorithmhub.com/
"""

import unittest
import error_funcs


class TestOverflow(unittest.TestCase):
    def setUp(self):
        pass

    def test_overflow(self):
        """
        Function to test where the passed value passes
        the OverflowError.

        Try with the following functions:
        overflow_math_error: will return assertion error
        overflow_other_error: will return assertion error
        overflow_no_error: will not return any error
        """

        try:
            error_funcs.overflow_no_error()
        except OverflowError:
            self.fail(
                "The given value doesn't fit the range"
            )


if __name__ == '__main__':
    unittest.main()
