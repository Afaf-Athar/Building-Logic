def sqaureofsortednum(nums):
    l = []
    for i in nums:
        i = i*i
        l.append(i)
        l.sort()
    return l


nums = [-4,-1,0,3,10]
print(sqaureofsortednum(nums))