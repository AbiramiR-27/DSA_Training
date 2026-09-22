"""Max Consecutive Ones II*
Problem Scenario: *Network Signal Stabilization*
A communication system records the status of a network connection for N consecutive time intervals.
•	1 represents a stable/active connection. 
•	0 represents a temporary connection failure. 
The system can recover at most one failed interval by treating one 0 as 1.
Your task is to find the maximum number of consecutive active intervals that can be obtained after recovering at most one failure.
Input Format
•	First line: An integer N, the number of intervals. 
•	Second line: N space-separated integers containing only 0 and 1. 
Output Format
Print a single integer representing the maximum number of consecutive 1s possible after changing at most one 0 into 1.
Constraints
•	1 ≤ N ≤ 100000 
•	Each element is either 0 or 1. 
•	At most one 0 can be changed to 1. """

n = 8
arr = [1, 0, 0, 0, 1, 0, 0, 1]

left = 0
zero_count = 0
maxi = 0
for right in range(n):
    if arr[right] == 0:
        zero_count += 1
        print(zero_count)
    while zero_count > 1:
        if arr[left] == 0:
            zero_count -= 1
            print(zero_count)
        left += 1
        print(left)
    maxi = max(maxi, right - left + 1)
    print(maxi)
print(maxi)