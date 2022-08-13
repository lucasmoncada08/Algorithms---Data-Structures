"""
Capacity to Ship Packages Within D Days

Given an array of weights, w, and a number of days to deliver the packages, d, return 
the minimum weight capacity of the truck.

Time Complexity: O(N + (logN)*N) = O(NlogN)
Space Complexity: O(1)
"""
from typing import List

def ship_in_d_days(weights: List[int], days: int) -> int:
    min_range = max(weights) # needs to carry at least this in one truck
    max_range = sum(weights) # at max will carry all in one truck

    least_capacity = -1

    while min_range <= max_range:
        mid = (min_range + max_range) // 2

        valid_capacity = _check_if_capacity_works(weights, days, mid)

        if valid_capacity:
            least_capacity = mid
            max_range = mid - 1
        else:
            min_range = mid + 1
        
    return least_capacity

# check if a given capacity is properly meets the days threshold
def _check_if_capacity_works(weights: List[int], days: int, capacity: int) -> bool:
    days_count = 1
    curr_capacity = capacity
    for w in weights:
        if curr_capacity >= w:
            curr_capacity -= w
        else:
            days_count += 1
            curr_capacity = capacity - w

    return days_count <= days
