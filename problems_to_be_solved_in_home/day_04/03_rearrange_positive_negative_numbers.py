"""
3) Rearrange array of +ve & -ve nums
"""
def rearrange(self, arr):
    pos = []
    neg = []
    for i in arr:
        if i >= 0:
            pos.append(i)
        else:
            neg.append(i)
    p = 0
    n = 0
    i = 0
    while p < len(pos) and n < len(neg):
        if i % 2 == 0:
            arr[i] = pos[p]
            p += 1
        else:
            arr[i] = neg[n]
            n += 1
        i += 1
    while p < len(pos):
        arr[i] = pos[p]
        p += 1
        i += 1
    while n < len(neg):
        arr[i] = neg[n]
        n += 1
        i += 1
    return arr

arr=[1,2,3,4,5,6,7,8,9,10]
print(rearrange(arr))