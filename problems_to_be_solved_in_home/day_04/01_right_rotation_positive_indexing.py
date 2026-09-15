"""
1) Right Rotation of Array using Positive indexing
"""

def rotate_right_index(arr, k):
    length = len(arr)
    if length == 0:
        return arr

    k = k % length
    rotated = [0] * length
    for i in range(length):
        new_index = (i + k) % length
        rotated[new_index] = arr[i]

    return rotated

arr = [23, 43, 45, 60, 46, 63]
k = 2
print(rotate_right_index(arr, k))
