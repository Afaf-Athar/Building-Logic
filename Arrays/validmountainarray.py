
# https://leetcode.com/problems/valid-mountain-array/discuss/1050492/PythonPython3-Valid-Mountain-Array

def validmountainarray(arr):

        
    arr_len = len(arr)
    if len(arr) <= 2:
        return False
    else:
        peak = arr.index(max(arr))
        if peak == len(arr) - 1 or peak == 0:
            return False

        left_inc = True
        right_inc = True


        for i in range(0,peak):

            if(arr[i]>= arr[i+1]):

                left_inc = False
                break

        for i in range(peak,arr_len-1):
            if(arr[i]<= arr[i+1]):
                right_inc = False
                break

    if(left_inc and right_inc): return True 
    return False

# arr = [0,2,4,5,3,2,1]
# arr = [3,5,5]
arr = [0,3,2,1]
# arr = [0,1,2,3,4,5,6,7,8,9]
print(validmountainarray(arr))