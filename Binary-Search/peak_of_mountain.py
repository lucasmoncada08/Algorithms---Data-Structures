"""
Peak of Mountain Array

Given an array of length >= 3 that increases and then decreases, find the peak

Time Complexity: O(logN)
Space Complexity: O(1)
"""
from typing import List

def peak_of_mountain(nums: List[int]) -> int:
    left, right = 0, len(nums)-1
    peak = 0
    nums.append(float('-inf')) # accounting for last element edge case

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] > nums[mid+1]:
            peak = mid
            right = mid - 1
        else:
            left = mid + 1
    
    nums.pop() # removing the added value
    
    return peak
        
        
         