"""
2) Left rotation using reverse algorithm
"""
def rotateArr(arr, d):
    n = len(arr)
    d = d % n
    if d == 0:
        return
    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    reverse(0, d - 1)
    print(arr)
    reverse(d, n - 1)
    print(arr)
    reverse(0, n - 1)
    print(arr)
    return arr


arr=list(map(int,input().split()))
print(rotateArr(arr,2))
