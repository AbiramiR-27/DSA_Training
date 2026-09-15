"""
7) Rearrange array such that arr[i] = i
"""

def modifyArray(arr):
    arr1 = [-1] * len(arr)
    for i in range(len(arr)):
        if i in arr:
            arr1[i] = i
    return arr1

arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
print(modifyArray(arr))
