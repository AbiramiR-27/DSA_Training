"""
2) Check if an Array is Sorted
"""
def isSorted(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
            break
    return True

arr=[1,2,3,4,5,6,7,8,9,10]
print(isSorted(arr))