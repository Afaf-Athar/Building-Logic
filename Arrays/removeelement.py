def removeelements(nums,val):

    i = 0
    len_nums = len(nums)
    while(i < len_nums):
        if(nums[i] == val):
            nums[i] = nums[i-1]
        i = i+1
        return nums
                
   


val = 2
nums = [1,2,2,3,1]
removeelements(nums,val)
# print(nums)