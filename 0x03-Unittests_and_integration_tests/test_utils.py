import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestStringMethods(unittest.TestCase):
    """
    implementing the first unittest to test the method of access_nested_map
        unittest: For creating and running tests.
        parameterized: For running the same test with different parameters.

    TestAccessNestedMap inherits from unittest.TestCase.
        @parameterized.expand decorator is used to provide different
        sets of inputs and expected outputs.

    test_access_nested_map takes nested_map, path, and expected as arguments.
    It asserts that the result of
    access_nested_map(nested_map, path) is equal to expected.
    using the assertEqual() method along with the function to test
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == "__main__":
    unittest.main()
