#!/usr/bin/env python3
"""testing for test_utils"""

import unittest

from parameterized import parameterized, parameterized_class

import utils


class TestAccessNestedMap(unittest.TestCase):
    """Test Class for testing utils"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, in1, in2, output):
        """test_access_nested_map method"""
        self.assertEqual(utils.access_nested_map(in1, in2), output)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, in2, in3, output):
        """test_access_nested_exception method"""
        self.assertRaises(output, utils.access_nested_map, in2, in3)


if __name__ == "__main__":
    unittest.main()
