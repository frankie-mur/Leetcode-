class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        L, R = 0, 0
        n = len(s)
        longest = 0
        
        while R < n:
            right = s[R]
            if right in seen:
                left = s[L]
                seen.remove(left)
                L += 1
                
            else:
                seen.add(right)
                R += 1
            
            longest = max(longest, R - L)
            
        return longest
                
                
                
        


            
                
                
            
                
                
                
            
        
    
            
          
        

