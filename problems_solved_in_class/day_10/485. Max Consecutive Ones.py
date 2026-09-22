'''Given a binary array nums, return the maximum number of consecutive 1's in the array.

 '''

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        c=0
        maxi=0
        for r in range(len(nums)):
            if nums[r]==1:
                c+=1
                maxi=max(maxi,c)
            else:
                c=0
        return maxi


"""class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        left = 0
        max_ones = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                # The streak is broken, move the start of the window
                left = right + 1
            else:
                # Calculate the size of the current valid window
                max_ones = max(max_ones, right - left + 1)
                
        return max_ones"""