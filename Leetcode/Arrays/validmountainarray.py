
# https://leetcode.com/problems/valid-mountain-array/discuss/1050492/PythonPython3-Valid-Mountain-Array

def validmountainarray(arr):
    arr_len = len(arr)
    max_ele = 0
    index = 0
    for i in range(arr_len):
        if arr[i] > max_ele:
            max_ele = arr[i]
            index = i
    print(max_ele)
    print(index)

    if(index ==0 or index == arr_len-1):
        return False
    

    for j in range(index):
        if(arr[j]>=arr[j+1] or arr[j]>max_ele):
           return False
    
    for j in range(index+1,arr_len-1):
        if(arr[j]<= arr[j+1] or arr[j]>= max_ele):
            return False
    
    return True

    # class Solution:
    #     def validMountainArray(self, arr: List[int]) -> bool:
        
    #     max_ind = -1
    #     mx = -1234
        
    #     for i in range(len(arr)):
    #         # finding peak value and peak index
    #         if (arr[i] >= mx):
    #             mx = arr[i]
    #             max_ind = i
        
    #     # peak can't be at extreme sides
    #     if max_ind == 0 or max_ind == len(arr)-1:
    #         return False
        
    #     # going upto peak index
    #     for j in range(max_ind):
    #         if arr[j] >= arr[j+1] or arr[j]>=mx: 
    #             return False
        
    #     # going down from peak index
    #     for j in range(max_ind+1, len(arr)-1):
    #         if arr[j] <= arr[j+1] or arr[j]>=mx: 
    #             return False
            
    #     return True

arr = [0,2,4,5,3,2,1]
validmountainarray(arr)