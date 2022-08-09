"""
First Element in Sorted Array with Duplicates

Given a sorted array and target value, find the first occurrence of the value.

Time Complexity: O(logN)
Space Complexity: O(1)
"""
from typing import List

def first_occurrence(nums: List[int], target: int) -> int:
    first_index = -1

    left, right = 0, len(nums)-1

    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            first_index = mid
        if nums[mid] >= target:
            if nums[mid] == target:
                first_index = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return first_index