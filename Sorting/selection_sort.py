"""
Selection Sort

Time Complexity: O(N^2)

Description:
A sorting algorithm that finds the current smallest element, one at a time, and then moves that
element to the currently sorted left side of the array.

"""

from typing import List

def selection_sort(nums: List[int]) -> List[int]:
    for i in range(len(nums)-1):
        low = float('inf')
        # for each index, find the minimum value on the right of the index
        for j in range(i, len(nums)):
            if nums[j] < low:
                switch = j
                low = nums[j]
        nums[i], nums[switch] = nums[switch], nums[i]
    
    return nums

