# def inplaceoperations(arr):

def no_element(arr,array_len):
    if(array_len ==1):
        arr[i] = -1
        print(arr)
    
    else:
        i = 0
        new_arr = arr[i:]
        maxi_arr = max(new_arr)
        arr[i] = maxi_arr
        i = i+1
        

arr = []
num = int(input())
for i in range(num):
    ele = int(input())
    arr.append(ele)
# print(arr)
array_len = len(arr)
# print(array_len)
no_element(arr,array_len)