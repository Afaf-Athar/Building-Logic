def searchandduplicate(arr):
    for i in range(0,len(arr)):
        for j in range(len(arr)):
            if i == j: continue
            if( arr[i] == 2* arr[j]):
                return True
        
    
arr = [10,2,5,3]
# arr = [7,1,14,11]
# arr = [3,1,7,11]
d = searchandduplicate(arr)
print(d)
