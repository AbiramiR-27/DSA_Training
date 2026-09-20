'''You are given an array arr of size n and an integer k. Your task is to find a pair of integers in the array such that it follows two conditions:

The sum of the pair is the maximum possible but less than k.
Out of all such pairs, choose the one with the maximum absolute difference between the two integers.
If no such pair exists, return (-1, -1).'''

class Solution:
    def maxSum(self, arr, k):
        arr.sort()
        l = 0
        r = len(arr) - 1

        max_sum = -1
        max_diff = -1
        res = [-1, -1]
        while l < r:
            c_sum = arr[l] + arr[r]
            if c_sum >= k:
                r -= 1
            else:
                diff = arr[r] - arr[l]
                if c_sum > max_sum:
                    max_sum = c_sum
                    max_diff = diff
                    res = [arr[l], arr[r]]
                elif c_sum == max_sum:
                    if diff > max_diff:
                        max_diff = diff
                        res = [arr[l], arr[r]]
                l += 1

        return res