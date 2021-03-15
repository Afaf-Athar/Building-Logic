# https://leetcode.com/explore/featured/card/fun-with-arrays/525/inserting-items-into-an-array/3245/

# def duplicatezeros(nums):
#     length = len(nums)
#     for i in range(0,length-1):
#         if(nums[i]== 0):
#             last = length - 1
#             while( i < last):
#                 nums[last] = nums[last-1]
#                 last = last-1
#             i = i+2
#         i=i+1    
# nums = [1,2,0,3,6]
# duplicatezeros(nums)
# print(nums)

def duplicatezeros(nums):
    # last = len(nums)-1
    # i =0
    # while(last>i):
    #     if(arr[i]==0):
    #         arr[last] = arr[last-1]
    #         last = last - 1
    #         i = i+1 
    #     i = i+1
    last = len(nums)-1
    i =0
    while(last>i):
        if(arr[i]==0):
            arr.pop()
            arr.insert(i+1,0)
            i += 1
        i = i+1
        

arr = [1,2,0,3,6]
#arr = [1,0,0,4,5]
#arr = [1, 0, 2, 3, 0, 4, 5, 0]
duplicatezeros(arr)
print(arr)