"""
5) Print All Pairs
"""
n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    for j in range(i + 1, n):
        print(f"({arr[i]},{arr[j]})")
