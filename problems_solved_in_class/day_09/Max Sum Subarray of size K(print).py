""" print all subarrays of size k """


arr=[1,2,3,4,5,6,7,8]
k=5
def sliding(arr):
  for i in range(len(arr)-k+1):
    for j in range(k):
      print(arr[i+j],end=" ")
    print()

sliding(arr)