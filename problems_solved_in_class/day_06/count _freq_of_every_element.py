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