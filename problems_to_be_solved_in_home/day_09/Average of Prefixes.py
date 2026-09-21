'''Given an array arr, find the floor of average of the prefix array at every index. '''

class Solution:
    def prefixAvg(self, arr):
        sum=0
        l=[]
        for i in range(len(arr)):
            sum +=arr[i]
            avg=sum //(i+1)
            l.append(avg)
        return l