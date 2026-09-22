'''Given an integer array arr[] and a number k. Find the count of distinct elements in every window of size k in the array.'''


"""
class Solution:
    def countDistinct(self, arr, k):
        l = []
        for i in range(len(arr)-k+1):
            l.append(len(set(arr[i:k+i])))
        return l
"""

from collections import Counter

class Solution:
    def countDistinct(self, arr, k):
        freq = Counter(arr[:k])
        res = [len(freq)]

        for i in range(k,len(arr)):

            freq[arr[i]]+=1

            outgoing = arr[i-k]
            freq[outgoing] -=1

            if freq[outgoing] == 0:
                del freq[outgoing]

            res.append(len(freq))

        return res