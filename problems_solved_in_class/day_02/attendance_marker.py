"""
Attendance marker - 0 for absent and 1 for present for N students

Different levels of difficulties:
- Input Validation
- Linear Time
- Using data as String only
"""

'''n = int(input())

for i in range(n):
    num = list(map(int,input().split()))
    count = 0
    for i in num:
        if i == 0:
            count+=1
    if count>0:
        print(str(count) + " student absent")
    else:
        print("No absentees")
'''

'''
n = int(input())
for i in range(n):
    num = input()
    count= num.count('0')
    if count>0:
        print(count,"student absent")
        print(count,"student absent out of",len(num),"student Att: ",((len(num)-count)/len(num))*100,"%")
    else:
        print("No absentees Att : 100%")
'''

n = int(input())
for i in range(n):
    num = input()
    length = 0
    count = 0
    for i in num:
        if i != " ":
            length+=1
            if i == '0':
                count+=1
    if count>0:
        print(count,"student absent")
        print(count,"student absent out of",length,"student Att: ",((length-count)/length*100),"%")
    else:
        print("No absentees Att : 100%")
