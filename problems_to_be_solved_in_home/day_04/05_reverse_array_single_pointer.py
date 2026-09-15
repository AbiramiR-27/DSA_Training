"""
5) Reverse array using single pointer
"""
def reverse_array(arr):
    for i in range(len(arr)//2):
        arr[i],arr[len(arr)-i-1]=arr[len(arr)-i-1],arr[i]
    return arr

arr=[1,2,3,4,5]
print(reverse_array(arr))