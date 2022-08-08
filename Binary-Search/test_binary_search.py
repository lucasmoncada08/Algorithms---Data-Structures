import unittest

from . import binary_search, binary_search_recursive

class TestBinarySearch(unittest.TestCase):
    binary_search_data = (
        ([1, 2, 3, 4, 5, 6, 7, 8], 1, 0),
        ([1, 2, 3, 4, 5, 6, 7, 8], 3, 2),
        ([1, 2, 3, 4, 5, 6, 7, 8], 4, 3),
        ([1, 2, 3, 4, 5, 6, 7, 8], 8, 7),
        ([1, 2, 3, 4, 5, 6, 7, 8], 6, 5),
        ([1, 2, 3, 4, 5, 6, 7], 4, 3),
        ([1, 2, 3, 4, 5, 6, 7], 1, 0),
        ([1, 3, 5, 6, 7, 10], 2, -1),
        ([3, 5, 5, 6, 9, 13], 8, -1),
        ([2, 5, 9], 0, -1),
        ([3, 4, 12, 134, 450], 1999, -1),
    )

    def test_binary_search(self):
        for data, target, expected in self.binary_search_data:
            actual = binary_search(data, target)
            self.assertEqual(expected, actual)
    
    def test_binary_search_recursive(self):
        for data, target, expected in self.binary_search_data:
            actual = binary_search_recursive(data, target)
            self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()