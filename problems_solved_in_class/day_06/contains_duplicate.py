def c_duplicate(arr):
    sets=set()
    for i in arr:
        if i in sets:
            return True
        sets.add(i)
    return False

arr = [1,2,3,4,5,6,7,8,9,10]
print(c_duplicate(arr))