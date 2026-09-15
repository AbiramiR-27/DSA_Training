"""
Analysis of Time complexity and space complexity for:
Reverse Array using Two Pointer

Time Complexity: O(n) - performs n // 2 swaps
Space Complexity: O(1) - in-place reversal
"""

def reverse_array_two_pointer(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

arr = [10, 20, 30, 40, 50]
print("Reversed Array:", reverse_array_two_pointer(arr))
