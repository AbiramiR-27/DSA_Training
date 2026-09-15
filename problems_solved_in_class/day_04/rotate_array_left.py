"""
Analysis of Time complexity and space complexity for:
Rotate Array (Left rotation)
"""

arr = [20, 30, 40, 50, 60, 70]
'''
k = 2
length = k % len(arr)
print(arr[k:] + arr[:k])
'''
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]

print(arr)