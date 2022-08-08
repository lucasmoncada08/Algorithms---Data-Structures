"""
Bubble Sort

Time Complexity: O(N)

Description:
A sorting algorithm that makes passes on the list, moving values from left to right. The sort
is complete when the algorithm makes one pass without switching elements

"""

from typing import List

def bubble_sort(nums: List[int]) -> List[int]:
    switch = True
    # until no switch occurs
    while switch:
        switch = False
        
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                switch = True
                nums[i], nums[i+1] = nums[i+1], nums[i]
    
    return nums
