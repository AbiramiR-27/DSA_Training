"""
Analysis of Time complexity and space complexity for:
First Last Occurrence of an element using Two Pointer

Time Complexity: O(n) - in the worst case, pointers scan through the array
Space Complexity: O(1) - in-place search using two pointers
"""

def first_last_occurrence(arr, target):
    left = 0
    right = len(arr) - 1
    first = -1
    last = -1

    while left <= right:
        if arr[left] == target and first == -1:
            first = left
        if arr[right] == target and last == -1:
            last = right
        
        if first != -1 and last != -1:
            break
        if first == -1:
            left += 1
        if last == -1:
            right -= 1

    return first, last

# Example test
arr = [1, 3, 5, 5, 5, 5, 67, 123, 125]
target = 5
first, last = first_last_occurrence(arr, target)
print(f"First Occurrence: {first}, Last Occurrence: {last}")
