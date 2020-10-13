  #O(N) time and O(N) Space
  def rob(self, nums: List[int]) -> int:
        n = len( nums )
        if n==0:
            return 0        
        if n==1:
            return nums[0]     
        if n==2:
            return max(nums[0],nums[1])  
        
        def max_profit(dp):     
            len_dp = len( dp )
            dp[1] = max( dp[0], dp[1] )
            for k in range( 2, len_dp ):
                dp[k] = max( dp[k - 1], dp[k] + dp[k - 2] )

            return dp[-1]        
        
        dp_excludingLastElement = nums[:n - 1]
        profit1 = max_profit(dp_excludingLastElement)
        dp_excludingFirstElement = nums[1:n]
        profit2 = max_profit(dp_excludingFirstElement)       
        return max( profit1, profit2 )
