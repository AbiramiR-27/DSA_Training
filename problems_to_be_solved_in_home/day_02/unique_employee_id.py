"""
Unique employee ID - "Yes" or "No"
"""

n = int(input())

for _ in range(n):
    num = list(map(int, input().split()))
    arr = []
    
    for i in num:
        if i in arr:
            print("No")
            break
        arr.append(i)
    else:
        print("Yes")
