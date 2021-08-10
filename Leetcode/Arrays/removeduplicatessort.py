def removeduplicatessort(nums):
    index = 1
    for i in range(1,len(nums)):
        if(nums[i-1]!=nums[i]):
            nums[index] = nums[i]
            index+=1
    return index


nums = [1,1,2,2,2,3,3,3,4,4]
print(removeduplicatessort(nums))
