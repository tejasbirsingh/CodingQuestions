    def rob(self, root: TreeNode) -> int:
        dp ={}     
                
        def rob_helper(root):
            if(not root):
                return 0
            if(root in dp.keys()):
                return dp[root]
            
            profit1 = rob_helper(root.left) + rob_helper(root.right)
            
            profit2 = root.val
            
            if(root.left is not None):
                profit2 += rob_helper(root.left.left) + rob_helper(root.left.right)
            
            if(root.right is not None):
                profit2 += rob_helper(root.right.left) + rob_helper(root.right.right)
                
            dp[root] = max(profit1,profit2)
            
            return dp[root]
        
            
        return rob_helper(root)
        
