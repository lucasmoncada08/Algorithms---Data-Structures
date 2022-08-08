"""
Insertion Sort

Time Complexity: O(N^2)

Description:
An intuitive sorting algorithm that comes from the idea of switching numbers from from 
right-to-left one-by-one until the end of the array/list.

"""
from typing import List

def insertion_sort(nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        j = i
        # move item left until left-adjacent is >=
        while j > 0 and nums[j] < nums[j-1]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1
            
    return nums
