"""
6) Rearrange array alternately
"""
def rearrange(arr):
    arr.sort()
    n = len(arr)
    temp = [0] * n
    left, right = 0, n - 1
    for i in range(n):
        if i % 2 == 0:
            temp[i] = arr[right]
            right -= 1
        else:
            temp[i] = arr[left]
            left += 1
    for i in range(n):
        arr[i] = temp[i]
    return arr

arr=[1,2,3,4,5,6,7,8,9,10]
print(rearrange(arr))