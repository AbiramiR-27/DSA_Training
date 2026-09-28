"""Given a string s, consisting of lowercase alphabets. Remove consecutive duplicate characters from the string. """


class Solution:
    def removeDuplicates(self, s):
        # code here
        res=[]
        for i in s:
            if not res or res[-1]!=i:
                res.append(i)
        return "".join(res)