def closest_pair(arr,n,t):
  l = 0 
  r = n-1
  l_min=0
  r_min=0
  min_diff=float('inf')
  while l < r: 
    add = arr[l] + arr[r]
    diff= abs(t - add)
    if min_diff > diff:
      min_diff=diff
      l_min = l
      r_min = r
      break
    if add < t :
      l += 1
    elif add > t:
      r -= 1
    else:
      break

  return (arr[l_min],arr[r_min])

print(closest_pair([-8,-2,3,6,12],5,1))
print(closest_pair([1,2,4,5,6,7,10,15],8,10))
print(closest_pair([1,3,6,8,11,14,18],7,20))
