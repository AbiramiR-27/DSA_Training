"check palindrome (linear TC and constant/linear SC)"

def palin(string_inp):
    
    string_inp = string_inp.lower()
    n = len(string_inp)
    for i in range(n//2):
        if string_inp[i]!= string_inp[n-i-1]:
            return False
    return True

string_input = input()
print(palin(string_input))

