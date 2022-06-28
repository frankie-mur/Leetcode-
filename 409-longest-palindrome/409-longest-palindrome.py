class Solution:
    def longestPalindrome(self, s: str) -> int:
        '''
        U-
        
        '''
        freq = Counter(s)
        longest = 0
        odd = False
        for val in freq.values():
            if val % 2 == 0:
                longest += val
            else:
                longest += val - 1
                odd = True
        
        if odd:
            longest += 1
            
        return longest
        
        
        
        
                