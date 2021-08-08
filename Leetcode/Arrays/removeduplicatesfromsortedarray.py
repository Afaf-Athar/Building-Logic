def removeduplicatedele(nums):
    # no_dup = []
    # for i in nums:
    #     if i not in no_dup:
    #         no_dup.append(i)
    # nums = no_dup
    # return nums

    i = 0
    while i < (len(nums)-1):
        if nums[i] == nums[i+1]:
            nums.remove(nums[i])
        else:
            i += 1

nums = [1,1,2]
removeduplicatedele(nums)
print(nums)