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


