class Solution:
    def reverseVowels(self, s: str) -> str:
        # O(N) Time and O(N) Space
#         stack = []
#         res = ""
#         for i in s:
#             if i.lower() in ['a','i','o','e','u']:
#                 stack.append(i)
                
#         for i in s:
#             if i.lower() in ['a','i','o','e','u']:
#                 res+= stack.pop()
#             else:
#                 res+=i
#         return res
    
#         O(N) Time and O(1) Space
        s=list(s)
        vowels="aeiouAEIOU"
        i=0
        j=len(s)-1
        while i<j:
            if s[i] in vowels and s[j] in vowels:
                    s[i],s[j]=s[j],s[i]
                    i+=1
                    j-=1
            else:
                if s[i] not in vowels:
                    i+=1
                if s[j] not in vowels:
                    j-=1

        return ''.join(s)
