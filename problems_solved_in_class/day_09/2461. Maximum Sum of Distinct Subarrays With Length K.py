"""You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array."""

class Solution(object):
    def maximumSubarraySum(self, nums, k):
        max_sum=0
        sums=0
        sets=set()
        l=0
        for r in range(len(nums)):
            while nums[r] in sets:
                sets.remove(nums[l])
                sums-=nums[l]
                l+=1
            sets.add(nums[r])
            sums+=nums[r]
            if r-l+1 > k:
                sets.remove(nums[l])
                sums-=nums[l]
                l+=1
                
            if r-l+1 == k:
                max_sum=max(max_sum,sums)

        return max_sum
