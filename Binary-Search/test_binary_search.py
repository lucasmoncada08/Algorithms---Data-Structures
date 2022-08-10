import unittest

from . import binary_search, binary_search_recursive, find_boundary, first_el_smaller, first_occurrence, \
    square_root, minimum_in_rotated

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

    find_boundary_data = (
        ([False, False, True, True], 2),
        ([False, False, False, True, True], 3),
        ([False, False, True, True, True], 2),
        ([False, False, False, True], 3),
        ([False, False, False, False, True], 4),
        ([False, True, True, True, True], 1),
        ([True, True, True, True], 0),
        ([False, False, False, False, False], -1),
        ([False], -1),
        ([True], 0),
    )

    first_el_smaller_data = (
        ([1, 2, 3, 4, 5, 6, 7, 8], 1, 0),
        ([1, 2, 3, 4, 5, 6, 7, 8], 3, 2),
        ([1, 2, 3, 4, 5, 6, 7, 8], 4, 3),
        ([1, 2, 3, 4, 5, 6, 7, 8], 8, 7),
        ([1, 2, 3, 4, 5, 6, 7, 8], 6, 5),
        ([1, 2, 3, 4, 5, 6, 7], 4, 3),
        ([1, 2, 3, 4, 5, 6, 7], 1, 0),
        ([1, 3, 5, 6, 7, 10], 2, 1),
        ([3, 5, 5, 6, 9, 13], 8, 4),
        ([2, 5, 9], 0, 0),
        ([3, 4, 12, 134, 450], 1999, -1),
        ([3, 4, 4, 4, 4, 12, 134, 450], 4, 1),
        ([3, 4, 4, 4, 4, 12, 134, 450], 3, 0),
        ([2, 6, 7, 10, 13, 13, 13, 13, 13, 19], 12, 4),
    )

    first_occurence_data = (
        ([1, 2, 3, 3, 3, 6, 8, 9], 3, 2),
        ([3, 5, 7, 7, 7, 7, 8], 7, 2),
        ([3, 4, 5, 8, 9, 9], 9, 4),
    )

    square_root_data = (
        (4, 2),
        (16, 4),
        (14, 3),
        (101, 10),
        (143, 11),
        (1, 1),
        (2, 1),
        (3, 1),
    )

    min_in_rotated_data = (
        ([3, 4, 5, 1, 2], 3),
        ([5, 1, 2, 3, 4], 1),
        ([3, 5, 7, 11, 13, 17, 19, 2], 7),
        ([1, 1, 1, 1, 1, 1], 0),
        ([2, 3, 4, 5, 6, 7], 0),
        ([3, 3], 0),
        ([9, 8], 1),
    )

    def test_binary_search(self):
        for data, target, expected in self.binary_search_data:
            actual = binary_search(data, target)
            self.assertEqual(expected, actual)
    
    def test_binary_search_recursive(self):
        for data, target, expected in self.binary_search_data:
            actual = binary_search_recursive(data, target)
            self.assertEqual(expected, actual)

    def test_find_boundary(self):
        for data, expected in self.find_boundary_data:
            actual = find_boundary(data)
            self.assertEqual(expected, actual)
    
    def test_first_el_smaller(self):
        for data, target, expected in self.first_el_smaller_data:
            actual = first_el_smaller(data, target)
            self.assertEqual(expected, actual)

    def test_first_occurence(self):
        for data, target, expected in self.first_occurence_data:
            actual = first_occurrence(data, target)
            self.assertEqual(expected, actual)

    def test_square_root(self):
        for num, expected in self.square_root_data:
            actual = square_root(num)
            self.assertEqual(expected, actual)

    def test_min_in_rotated(self):
        for data, expected in self.min_in_rotated_data:
            actual = minimum_in_rotated(data)
            self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()