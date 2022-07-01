class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        U- Given s and k we must find the longest substring containing the same char given that we can change a char k times within that substring.
        M- Hashmap, sliding window
        P- 
             
        '''
        
        res, l,maxfreq = 0, 0, 0
        counts = {}
        
        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            maxfreq = max(maxfreq, counts[s[r]]) 
            while (r - l + 1 - maxfreq > k):
                counts[s[l]] -= 1
                l += 1
                
            res = max(res, r - l + 1)
        return res
        