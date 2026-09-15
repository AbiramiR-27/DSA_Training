"""
8) Rearrange array with O(1) extra space
"""
def arrange(arr):
    n = len(arr)
    for i in range(n):
        arr[i] = arr[i] + (arr[arr[i]] % n) * n
    for i in range(n):
        arr[i] = arr[i] // n

    return arr

arr=[1,2,3,4,5]
print(arrange(arr))