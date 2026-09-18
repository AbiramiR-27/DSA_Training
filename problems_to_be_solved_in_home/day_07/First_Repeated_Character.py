'''Given a string s. The task is to find the first repeated character in it. We need to find the character that occurs more than once and whose index of second occurrence is smallest. s contains only lowercase letters.
'''
class Solution:
    def firstRepChar(self, s):
        t=''
        for i in s:
            if i in t:
                return i
            t=t+i
        else:
            return -1