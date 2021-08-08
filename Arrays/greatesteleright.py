def greatesteleright(arr):
    arr_len = len(arr)
    if(arr_len == 0):
        return -1
    
    for i in range(arr_len):
        if(i == arr_len-1):
            arr[i] = -1
        else:
            slice_arr = arr[i+1:]
            max_slice_arr = max(slice_arr)
            arr[i] = max_slice_arr
    
    return (arr)

arr = [17,18,5,4,6,1]
# arr = [0,3]
# arr = [0,1,2,3,4,5,6,7,8,9]
print(greatesteleright(arr))