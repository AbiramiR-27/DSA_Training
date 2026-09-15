"""
Analysis of Time complexity and space complexity for:
Reverse Array

Time Complexity: O(n) - visits each element once
Space Complexity: O(n) - for creating a new reversed array
"""

def reverse_array(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

arr = [1, 2, 3, 4, 5]
print("Original Array:", arr)
print("Reversed Array:", reverse_array(arr))
