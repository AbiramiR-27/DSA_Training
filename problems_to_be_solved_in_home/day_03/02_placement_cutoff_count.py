"""
2) Placement Cutoff Count
"""

n = int(input())
c = int(input())
scores = list(map(int, input().split()))
count = 0
for i in scores:
    if i >= c:
        count += 1
print(count)
