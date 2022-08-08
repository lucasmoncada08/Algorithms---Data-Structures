"""
Binary Search

Time Complexity: O(logN)

Description:
An algorithm to find an element in an already sorted array. The algorithm chooses a middle point to 
compare to the target, if the target is less than, the left is searched, and if the target is greater
than, the right is searched. This happens until the target is found or the current search 
half is empty.

This can be implemented iteratively or recursively, both are shown below.

"""

from typing import List

def binary_search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)-1

    while left <= right:
        mid = (left + right) // 2
        
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid-1
        else:
            left = mid+1
    
    return -1


def binary_search_recursive(nums: List[int], target: int) -> int:
    return _binary_search_helper(nums, target, 0, len(nums)-1)

def _binary_search_helper(nums: List[int], target: int, left: int, right: int) -> int:
    if left > right:
        return -1
    
    mid = (right + left) // 2

    if target == nums[mid]:
        return mid
    elif target < nums[mid]:
        return _binary_search_helper(nums, target, left, mid-1)
    else:
        return _binary_search_helper(nums, target, mid+1, right)


"""
Examples

  [1, 2, 3, 4, 5, 6, 7, 8]
    target = 8

    left = 4
    right = 7
    mid = 5



  [1, 2, 3, 4, 5, 6, 7]

"""
