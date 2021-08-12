def removezeros(nums):
    if(len(nums)==1):
        return nums

    j = len(nums)-1
    i = 0
    while(i<j):
        if(nums[i]>nums[i+1]):
            temp = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = temp
        if(nums[i] == 0 and nums[j]!=0):
            k = nums[i]
            nums[i] = nums[j]
            nums[j] = k
            # if(nums[i]>nums[i+1]):
            #     temp = nums[i]
            #     nums[i] = nums[i+1]
            #     nums[i+1] = temp
            j = j-1
        else:
            i = i+1

    return nums
                  
nums = [0,1,0,3,12]
print(removezeros(nums))