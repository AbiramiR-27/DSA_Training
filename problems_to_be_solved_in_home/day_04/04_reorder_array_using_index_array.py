"""
4) Reorder array using index array
"""

def reorder_arr(arr, ind_arr):
    arr1 = [0] * len(arr)
    for i in range(len(arr)):
        arr1[ind_arr[i]] = arr[i]
    return arr1

arr = [12, 3, 54, 55, 65]
ind_arr = [1, 3, 4, 2, 0]
print(reorder_arr(arr, ind_arr))
