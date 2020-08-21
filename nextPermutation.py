def nextPermutation(nums) :
        
    i = len(nums) - 2
    
    while i >= 0 and nums[i + 1] <= nums[i]:
        i -= 1
        
    if i != -1:
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
            
        nums[i], nums[j] = nums[j], nums[i]
        
    nums[i + 1:] = nums[:i:-1] if i != -1 else reversed(nums)



nums=[4,1,5,3,2]
nextPermutation(nums)
print(nums)