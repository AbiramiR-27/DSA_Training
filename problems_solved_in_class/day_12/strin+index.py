"get a input string from the user and the print the index + char"


def str_ind(str):
  for i in range(len(str)):
    print(str[i],":",i )


try:
    n = input("Enter the string: ")
    str_ind(n)
except:
    print("Enter a valid string")
    