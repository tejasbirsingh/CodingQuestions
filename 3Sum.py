 
# Time - O(n^2) and Space - O(1)
def threeSum(nums):                 
        nums.sort()
        res = []
        n = len(nums)
        for i in range(0,n-2):  
            # if value at previous index is same then skips this index
            if i>0 and nums[i]==nums[i-1]:
                continue 
            l, r = i+1, n-1             
            while l<r:
                total = nums[i]+nums[l]+nums[r]

                if total==0: 
                    res.append([nums[i], nums[l], nums[r]])
                    # Skip all the value which are same as array is same so duplicate values occur together
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]: 
                        r-=1
                    l+=1
                    r-=1
                    
                elif total<0: 
                    l+=1
                else: 
                    r-=1
        return res


a=[-1, 0, 1, 2, -1, -4]
res = threeSum(a)
for i in res:
    print(*i)