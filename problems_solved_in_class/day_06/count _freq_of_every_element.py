def count_freq(num):
  dict={}
  n=len(num)
  for i in range(n):
    dict[num[i]] = dict.get(num[i], 0)+1
  return dict
  
n = list(map(int,input().split()))
print(count_freq(n))

'''def count_freq(num):
  dict={}
  n=len(num)
  for i in range(n):
    dict[num[i]] = dict.get(num[i], 0)+1
  return dict
  
n = input()
print(count_freq(n))'''

'''def occ(arr,n):
    count=0
    for i in arr:
        if i == n:
            count+=1
    return count

try:
    n=input()
    print(occ('helllo',n))
except:
    print('enter a valid input')'''