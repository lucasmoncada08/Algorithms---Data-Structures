"""
Find the boundary between an array of Falses and Truths, where the falses are on the left and 
truths on the right.

Ex. [False, False, True, True]

Time Complexity: O(logN)
Space Complexity: O(1)

"""

from typing import List

def find_boundary(vals: List[bool]) -> int:

    left = 0
    right = len(vals)-1

    while left <= right:
        mid = (left + right) // 2

        if vals[mid]:
            if not vals[mid-1] or mid == 0:
                return mid
            right = mid - 1
        else:
            left = mid + 1
    
    return -1

