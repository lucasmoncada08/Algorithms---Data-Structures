import unittest

from insertion_sort import insertion_sort
from selection_sort import selection_sort

class TestSorting(unittest.TestCase):
    data = [
        [3, 2, 4, 1],
        [1],
        [9, 2, 4, 1, 1, 1, 5, 3],
        [],
        [-12, 3, 5, 1, -4],
        [100, 0, 1, 3, 81, -1, 0]
    ]

    def test_insertion_sort(self):
        for nums in self.data:
            expected = sorted(nums)
            actual = insertion_sort(nums)
            self.assertEqual(expected, actual)
    
    def test_selection_sort(self):
        for nums in self.data:
            expected = sorted(nums)
            actual = selection_sort(nums)
            self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
