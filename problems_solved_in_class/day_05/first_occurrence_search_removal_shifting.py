"""
First occurrence search, removal and element shifting (static & dynamic array)
"""

''' Delete First Occurrence of Given Element from an Array
Given an array of integers, the task is to delete a given
element from the array. If there are multiple occurrences of
the element, we need to remove only its first occurrence.'''

def first_occ(arr, ele):
    for i in range(len(arr)):
        if arr[i] == ele:
            for j in range(i, len(arr) - 1):
                arr[j] = arr[j + 1]
            return arr[:len(arr) - 1]
    else:
        return arr

print(first_occ([3, 4, 6, 7, 8, 9, 10], 6))
