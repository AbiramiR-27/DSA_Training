"""
Array - min / max
"""

def min_max(arr):
    mini=arr[0]
    maxi=arr[0]
    for i in range(len(arr)):
        if arr[i]>maxi:
            maxi=arr[i]
        if arr[i]<mini:
            mini=arr[i]
    print("Min:",mini)
    print("Max:",maxi)

arr=[2,3,4,5,3,2,6,1,9,8,7]
min_max(arr)
