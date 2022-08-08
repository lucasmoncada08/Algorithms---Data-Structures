"""
Merge Sort

Time Complexity: O(NlogN)

Description:
A sorting algorithm that implements divide and conquer. The algorithm recursively splits the left 
and right side of the current array until getting individual elements. At this point the algorithm
traverses back up the stack using a merge function to sort the resultant left and right sides.

"""

from typing import List

def merge_sort(nums: List[int]) -> List[int]:

    if len(nums) <= 1:
        return nums
    
    if len(nums) % 2 == 0:
        mid = len(nums) // 2
    else:
        mid = len(nums) // 2 + 1
    
    # recursive get left and right sides
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return _merge(left, right)
    
# function for merging the left and right side using an extra list
def _merge(left, right):
    res = []
    
    l_ind = r_ind = 0
    while l_ind < len(left) and r_ind < len(right):
        if left[l_ind] <= right[r_ind]:
            res.append(left[l_ind])
            l_ind += 1
        else:
            res.append(right[r_ind])
            r_ind += 1
    
    while l_ind < len(left):
        res.append(left[l_ind])
        l_ind += 1
    
    while r_ind < len(right):
        res.append(right[r_ind])
        r_ind += 1
    
    return res