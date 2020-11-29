  def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        mod = sum(nums)%p
        if mod==0:
            return 0        
        res = n
        s = 0
        hashmap = {0: -1}
        
        for i, num in enumerate(nums):            
            s += num
            key = (s%p - mod)
            # key = key % p
            if key<0:
                key +=p              
            
            if key in hashmap:
                res = min(res, i-hashmap[key])
            
            hashmap[s%p] = i
            
        
            
        return res if res < n else -1
