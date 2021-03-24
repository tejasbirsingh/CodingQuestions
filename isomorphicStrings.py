 # O(N) Time and O(N) Space
 def isIsomorphic(self, s: str, t: str) -> bool:
	    
        n = len(s)
        m = len(t)
        
        if(n != m):
            return False
        
        d = {}	
        visited = set()

        for i in range(n):
	
            if s[i] in d:            
                if d[s[i]] != t[i]:
                    return False                
		
            elif t[i] in visited:
                return False
            
            else:		
                d[s[i]] = t[i]
                visited.add(t[i])
                
        return True
