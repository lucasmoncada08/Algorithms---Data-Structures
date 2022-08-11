"""
Peak of Mountain Array

Given an array of length >= 3 that increases and then decreases, find the peak

Time Complexity: O(logN)
Space Complexity: O(1)
"""
from typing import List

def peak_of_mountain(nums: List[int]) -> int:
    left, right = 1, len(nums)-2

    while left <= right:
        mid = (left + right) // 2

        if nums[mid-1] < nums[mid] < nums[mid+1]:
            return mid
        
        if nums[left] < nums[mid]:
            if nums[mid-1] < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
            continue
        
        if nums[mid] > nums[right]:
            if nums[mid] > nums[mid+1]:
                right = mid - 1
            else:
                left = mid + 1
    
            
         