''' You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.'''

from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        l = []
        s = deque()
        for i in range(len(nums)):
            if s and s[0] < i - k + 1:
                s.popleft()

            while s and nums[s[-1]] < nums[i]:
                s.pop()

            s.append(i)
            
            if i >= k - 1:
                l.append(nums[s[0]])
                
        return l