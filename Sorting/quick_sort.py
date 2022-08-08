"""
Quick Sort

Time Complexity: Avg -> O(NlogN), Worst -> O(N^2)

Description:
Quick sort is a recursive sorting algorithm that uses pivot points to sort the pivot so that 
the left side of that pivot has elements smaller and the right side has elements greater to or
equal. Then the left and right sides are sorted recursively using the same method.

"""

from typing import List

def quick_sort(nums: List[int]) -> List[int]:
    return _quick_sort_helper(nums, 0, len(nums))

def _quick_sort_helper(nums: List[int], start: int, end: int) -> None:
    if end - start <= 1:
        return nums
    
    pivot = nums[end-1]
    left = start
    right = end-1

    while left < right:
        while nums[left] < pivot and left < right:
            left += 1
        while nums[right] >= pivot and left < right:
            right -= 1
        # left is less and right is greater than pivot
        if left == right:
            break
        nums[left], nums[right] = nums[right], nums[left]
    
    nums[left], nums[end-1] = nums[end-1], nums[left]
    _quick_sort_helper(nums, start, left) # sort left side
    _quick_sort_helper(nums, left+1, end) # sort right side
    return nums


vals = [3, 5, 5, 1, 9, 2, 10]

print(quick_sort(vals))
