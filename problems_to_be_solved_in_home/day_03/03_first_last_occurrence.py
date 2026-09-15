"""
3) First Last Occurrence of an element
"""
n, x = map(int, input().split())
arr = list(map(int, input().split()))
first = -1
last = -1
for i in range(n):
    if arr[i] == x:
        if first == -1:
            first = i
        last = i
print(first, last)
