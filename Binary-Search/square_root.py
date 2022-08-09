"""
Square Root

Implement the square root function without the use of the built in square root function.

Time Complexity: O(logN)
Space Complexity: O(1)
"""

def square_root(num: int) -> int:
    low_val = 1

    left, right = 1, num-1

    while left <= right:
        mid = (left + right) // 2

        square = mid**2

        if square == num:
            return mid
        elif square < num:
            low_val = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return low_val
