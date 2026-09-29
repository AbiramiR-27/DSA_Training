def str_num(str):
    nums=[]
    ops=[]
    for i in str:
        if i.isdigit():
            nums.append(i)
        else:
            ops.append(i)
    print(nums)
    print(ops)
    
n=input()
str_num(n.split())
