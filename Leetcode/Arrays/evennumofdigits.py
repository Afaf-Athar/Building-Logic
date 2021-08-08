# def returnlength(num):
#     lencount = 0
#     while(num>0):
#         rem = num%10
#         num = num//10
#         lencount = lencount + 1
#     return lencount

# def evennumofdigits(nums):
#     evecount = 0
#     # oddcount = 0
#     for i in nums:
#         l = returnlength(i)
#         if( l % 2 == 0):
#             evecount = evecount + 1
#         # else:
#         #     oddcount = oddcount + 1
#     return evecount

# nums = [555,901,482,1771]


def evennumofdigits(nums):
    evecount = 0
    for i in nums:
        lencount = 0
        while(i>0):
            i = i//10
            lencount = lencount + 1
        if(lencount % 2 == 0):
            evecount = evecount + 1
    return evecount

nums = [437,315,322,431,686,264,442]
# print(nums.count(1))
# print(len(nums))
print(evennumofdigits(nums))