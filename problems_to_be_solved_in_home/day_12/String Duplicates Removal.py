'''Given a string s which may contain lowercase and uppercase characters. The task is to remove all duplicate characters from the string and find the resultant string. The order of remaining characters in the output should be same as in the original string.'''


class Solution:

	
	def removeDuplicates(self, s):
	    sets=set()
	    l=''
	    for i in s:
	        if i not in sets :
	            l=l+i
	        sets.add(i)
	    return l