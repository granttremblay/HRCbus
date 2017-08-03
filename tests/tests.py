#!/usr/bin/env python

from context import hrcbus

import unittest


class BasicTestSuit(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
        assert True

    def test_check_environment(self):
        hrcbus.check_environment()
        pass


if __name__ == '__main__':
    unittest.main()
