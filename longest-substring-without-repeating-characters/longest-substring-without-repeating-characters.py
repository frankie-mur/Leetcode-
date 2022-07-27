class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        res = 0
        w_start, w_end = 0, 0
        while w_end < len(s):
            rch = s[w_end]
            if rch not in seen:
                res = max(res, w_end - w_start + 1)
                print(res)
                w_end += 1
                seen.add(rch)
            else: 
                lch = s[w_start]
                seen.remove(lch)
                w_start += 1                
            
        return res

            
                
                
            
                
                
                
            
        
    
            
          
        

