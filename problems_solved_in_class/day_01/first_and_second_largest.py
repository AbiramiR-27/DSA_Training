"""
Array - first largest, second largest
"""

def largest(arr):
    first=-1
    second=-1
    for i in range(len(arr)):
        if arr[i]>first:
            second=first
            first=arr[i]
        elif arr[i]>second and arr[i]!=first:
            second=arr[i]
    return first,second

arr=[1,2,3,4,5,6,7,8,9,10]
first,second=largest(arr)
print("First largest:",first)
print("Second largest:",second)
