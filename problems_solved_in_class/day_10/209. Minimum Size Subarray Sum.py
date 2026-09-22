""" Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 """

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l=0
        min_len=float('inf')
        sum=0
        for r in range(len(nums)):
            sum+=nums[r]
            while sum>=target:
                min_len=min(min_len,r-l+1)

                sum-=nums[l]
                l+=1

        if min_len == float('inf'):
            return 0
        
        return min_len