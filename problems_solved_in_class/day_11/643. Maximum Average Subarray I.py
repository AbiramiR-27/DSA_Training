"""You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 """

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        sums=sum(nums[:k])
        max_avg=sums
        for i in range(len(nums)-k):
            sums+=nums[k+i]-nums[i]
            max_avg=max(max_avg,sums)

        return  max_avg/k