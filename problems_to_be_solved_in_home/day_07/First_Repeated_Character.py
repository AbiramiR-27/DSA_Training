class Solution:
    def firstRepChar(self, s):
        t=''
        for i in s:
            if i in t:
                return i
            t=t+i
        else:
            return -1