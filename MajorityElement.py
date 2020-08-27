def majorityElement(nums):
    
    count =0
    element = 0
    for i in nums:
        if count ==0:
            element = i
        if element == i:
            count+=1
        else:
            count-=1
            
    return element


arr = [1,2,2,1,1,2,2,2]
print(majorityElement(arr)) 