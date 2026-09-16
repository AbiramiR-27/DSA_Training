'''Problem:
After reading each element, print the maximum value seen so far.

Input:
2 5 1 8 3

output:
2 5 5 8 8'''

def max_ele(arr):
  max=arr[0]
  for i in range(len(arr)):
    if arr[i]>max:
      max=arr[i]
    else:
      arr[i]=max
  return arr

arr=list(map(int,input().split()))
print(max_ele(arr))