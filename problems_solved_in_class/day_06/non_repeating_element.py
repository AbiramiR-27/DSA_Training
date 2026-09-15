def firstNonRepeating(arr): 
        dict={}
        for i in arr:
            dict[i]=dict.get(i, 0)+1
        for i in dict:
            if dict[i]==1:
                return i
        else:
            return 0 

arr=[1,2,3,2,1,5,6,7,8,9,10]
print(firstNonRepeating(arr))