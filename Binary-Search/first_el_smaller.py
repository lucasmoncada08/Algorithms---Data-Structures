
"""
First Element Not Smaller Than Target
- Array of integers sorted with target, return index
- Assume guarantee number

Time Complexity: O(logN)
"""

from typing import List

# practically binary search but adds the min_ind to track the desired index
def first_el_smaller(nums: List[int], target: int) -> int:
    min_ind = -1

    left, right = 0, len(nums)-1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] >= target:
            min_ind = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return min_ind



"""
Tests:

[1, 2, 4, 6, 9, 13],
4

left = 1
right = 1
min_ind = 2
mid = 2


[0, 3, 9, 14, 14]


"""