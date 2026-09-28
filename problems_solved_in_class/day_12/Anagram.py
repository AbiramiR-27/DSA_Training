""" Given two non-empty strings s1 and s2, consisting only of lowercase English letters, determine whether they are anagrams of each other or not.
Two strings are considered anagrams if they contain the same characters with exactly the same frequencies, regardless of their order."""
'''

class Solution:
    def areAnagrams(self, s1, s2):
       # code here
        dict1={}
        dict2={}
        if len(s1)!=len(s2):
           return False
        else:
            for i in range(len(s1)):
                dict1[s1[i]]= dict1.get(s1[i],0)+1
                dict2[s2[i]]= dict2.get(s2[i],0)+1
            if dict1==dict2:
                return True
'''

'''        dict={}
        if len(s1)!=len(s2):
            return False
        else:
            for i in s1:
                s1[i]=dict1.get(s[i],0)+1
            for i in s2:
                if i not in dict.keys():
                    return False
                dict[i]=dict.get(s2[i],0)-1
                if dict[i]==0:
                    del dict[i]
            return True'''

def arr_sol(s1,s2):
    if len(s1)!=len(s2):
        return False
    arr=[0]*26
    for i in s1:
        arr[ord(i)-ord('a')]+=1
    for i in s2:
        arr[ord(i)-ord('a')]-=1
    if arr==[0]*26:
        return True
    else:
        return False

s1=input()
s2=input()
print(arr_sol(s1,s2)) 













