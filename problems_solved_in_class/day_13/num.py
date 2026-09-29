def str_int(str):
    a=str.split(" ")
    x,y=int(a[0]),int(a[2])
    op=a[1]
    try:
        if op=="/":
            s=x//y
            r=x%y
            print(s,r)
        elif op=="*":
            s=x*y
            print(s)
        elif op=="+":
            s=x+y
            print(s)
        elif op=="-":
            s=x-y
            print(s)
    except Exception as e:
        print(e)

n=input()
str_int(n)

"""
import operator

operations={
    "+":operator.add,
    "-":operator.sub,
    "*":operator.mul,
    "/":operator.truediv
}

def eval_exp(expr):
    a=expr.split(" ")
    x,y=int(a[0]),int(a[2])
    op=a[1]
    if op in operations:
        return operations[op](x,y)
    else:
        return "Invalid operator"

print(eval_exp("256 + 72"))

"""

s = input()

s_splitted = []
word = ""

for i in s:
    if i == " ":
        if word:
            s_splitted.append(word)
            word = ""
    else:
        word += i

if word:
    s_splitted.append(word)

n1 = int(s_splitted[0])
operator = s_splitted[1]
n2 = int(s_splitted[2])

if operator == "+":
    print("Sum:", n1 + n2)
elif operator == "-":
    print("Difference:", n1 - n2)
elif operator == "*":
    print("Product:", n1 * n2)
elif operator == "/":
    print("Quotient:", n1 // n2)
    print("Remainder:", n1 % n2)
else:
    print("Invalid")     


