"""
model_test_recursionandrun.py

Unit tests to demonstrate recursion and run time error for model.

AlgorithmHub. All rights reserved.
https://www.algorithmhub.com/
"""

import unittest
import error_funcs


class TestType(unittest.TestCase):
    def setUp(self):
        pass

    def test_recursion_run(self):
        """
        Function to test where the passed value passes
        the RuntimeError.

        Try with the following functions:
        type_error(-1, 2, '3'): will return assertion error
        type_error(1, 2, 3): will not return any error
        """

        def recursion_test_error():
            "Function to demonstrate recursion error"

            return recursion_test_error()

        def recursion_test_no_error():
            "Function to demonstrate no recursion error"

            pass

        try:
            error_funcs.recursion_run_error(recursion_test_error)
        except RuntimeError as e:
            if str(e) == 'maximum recursion depth exceeded':
                self.fail(
                    "You can't recursively call a function for more than 1000 times"
                )
            else:
                self.fail(
                    "Encountered the following RuntimeError: {}".format(str(e))
                )


if __name__ == '__main__':
    unittest.main()
