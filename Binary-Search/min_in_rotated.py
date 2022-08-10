"""
Find the Minimum in Rotated Sorted Array

The array has been rotated at an unknown pivot, find the index of the minimum element in array.

Time Complexity: O(logN)
Space Complexity: O(1)
"""

from typing import List

def minimum_in_rotated(nums: List[int]) -> int:
    if nums[0] <= nums[len(nums)-1]:
        return 0
    
    left, right = 1, len(nums)-1

    while left <= right:

        mid = (left + right) // 2

        if nums[mid-1] > nums[mid]:
            return mid
        elif nums[mid] > nums[right]:
            left = mid+1
        else:
            right = mid
        
    
"""
[3, 4, 5, 1, 2]

left = 3
right = 4
mid = 3

[5, 1, 2, 3, 4]

left = 1
right = 2
mid = 1

[3, 5, 7, 11, 13, 17, 19, 2]

left = 7
right = 7

mid = 6

"""


