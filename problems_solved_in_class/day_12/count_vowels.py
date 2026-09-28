" Count vowels , consonants the string will contains alphabets and upper and lower case chars"

def count_vow_con(string_inp):
    vowels = {"a": 1, "e":1,"i":1,"o":1,"u":1}
    vow,con=0,0
    for i in string_inp:
        if i in vowels.keys():
            vow+=1
        else:
            con+=1
    print("Vowels count:",vow)
    print("Cons:",con)

string = input()
count_vow_con(string.lower())


