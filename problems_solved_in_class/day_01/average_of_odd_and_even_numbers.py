"""
Average of Odd numbers and Even numbers

Different levels of difficulties:
- Input Validation
- Output round off to 2 decimal places
"""

arr=[1,2,3,4,5,6,7,8,9,10]
sum_even=0
sum_odd=0
count_even=0
count_odd=0
for i in range(len(arr)):
    if arr[i]%2==0:
        sum_even+=arr[i]
        count_even+=1
    else:
        sum_odd+=arr[i]
        count_odd+=1
avg_even=sum_even/count_even
avg_odd=sum_odd/count_odd
print("Average of even numbers:",avg_even)
print("Average of odd numbers:",avg_odd)
