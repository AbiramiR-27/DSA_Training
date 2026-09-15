"""
Analysis of Time complexity and space complexity for:
Rotate Array (Right rotation using negative indexing)

Time Complexity: O(n) - array slicing and concatenation
Space Complexity: O(n) - creates a new list from slices
"""

def rotate_right_negative_indexing(arr, k):
    if not arr:
        return arr
    k = k % len(arr)
    if k == 0:
        return arr
    return arr[-k:] + arr[:-k]

arr = [10, 20, 30, 40, 50, 60]
k = 2
print("Original:", arr)
print(f"Rotated by {k}:", rotate_right_negative_indexing(arr, k))
