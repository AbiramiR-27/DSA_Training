'''Given an array of integers arr[]  and a number k. Return the maximum sum of a subarray of size k.'''

class Solution:
    def maxSubarraySum(self, arr, k):
        curr=max_sum=sum(arr[:k])
        for i in range(1, len(arr)-k+1):
            curr+=arr[i+k-1]-arr[i-1]
            max_sum=max(curr,max_sum)
        return max_sum