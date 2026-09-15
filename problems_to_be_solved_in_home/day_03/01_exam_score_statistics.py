"""
1) Exam Score Statistics
"""
n = int(input())
num = list(map(int, input().split()))
sumf = 0
print("Scores:")
for i in range(n):
    print(num[i], end=' ')
    if (i + 1) % 4 == 0:
        print()
for i in range(n):
    sumf += num[i]
average = sumf / n
print(f"\nAverage: {average:.2f}")
print("Lowest Score:", min(num))
print("Highest Score:", max(num))
print("\nScore  Deviation")
sumsd = 0
for i in num:
    deviation = i - average
    print(f"{i}     {deviation:.2f}")
    sumsd += deviation * deviation
SD = (sumsd / n) ** 0.5
print(f"\nStandard Deviation: {SD:.2f}")
count = 0
for i in num:
    if average - SD <= i <= average + SD:
        count += 1
print("Scores within one standard deviation:", count)
