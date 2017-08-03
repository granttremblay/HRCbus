#!/usr/bin/env python

from .context import hrcbus

import unittest

class BasicTestSuit(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
	assert True

if __name__ = '__main__':
    unittest.main()
