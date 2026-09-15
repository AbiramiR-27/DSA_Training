"""
Application of Time complexity and space complexity on Fibonacci Series
"""

try:
    n = int(input())
    x = 0
    y = 1
    if n == 1:
        print(x)
    else:
        print(x, y, end=' ')
        for i in range(2, n):
            x, y = y, x + y
            print(y, end=' ')
except:
    print("Invalid input")
