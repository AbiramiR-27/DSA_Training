
'''Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.'''

class Solution(object):
    def firstUniqChar(self, s):
        t={}
        for i in s:
            t[i]=t.get(i,0)+1
        for i in range(len(s)):
            if t[s[i]]==1:
                return i
        else:
            return -1