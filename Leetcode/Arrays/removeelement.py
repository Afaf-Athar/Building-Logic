
#https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3247/

def removeelements(nums,val):
    i = 0
    len_nums = len(nums)
    while(i < len_nums):
        if(nums[i] == val):
            nums.remove(nums[i])
            len_nums = len_nums-1
            i = i-1
        i = i+1
   


val = 2
nums = [1,2,2,3,1]
removeelements(nums,val)
print(nums)