def mergesortedarray(nums1,nums2,m,n):
    # total_len = len(nums2) + len(nums2)
    # arr = []
    # i = j = k = 0
    # while(total_len!=0):
    #     if(nums1[i]>=nums2[j]):
    #         arr[k] = nums1[i]
    #         i += 1
    #     else:
    #         arr[k] = nums2[j]
    #         j += 1
    #     k += 1
    # return arr
    for i in range(n):
        nums1[i+m] = nums2[i]
        
    nums1.sort()
        
m = 3
n = 3
nums1 = [1,4,5]
nums2 = [1,2,3]
mergesortedarray(nums1,nums2,m,n)
print(mergesortedarray)