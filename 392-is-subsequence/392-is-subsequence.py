class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
        U- Retun if s is a subsequence of t, subsequence is a string that is formed by deleting chars from t and s == t w/o moving relative postitions of chars
        M- two pointer
        P- Have two pointers for both strings if chars are equal move both pointers and if t has a diff char only move p2, in the end if p1 is equal to the length of s we have a subsequence
        I- python
        R- Passes test cases but I fear there may be some edge cases
        E- Time: O(n) one pass through both strings
           Space: O(1) only use ints to store pointers through strings
        
        '''
        
        if not s and t:
            return True
        
        p1, p2 = 0, 0 
        while p2 < len(t):
            sch, tch = s[p1], t[p2]
            if sch != tch:
                p2 += 1
            else:        
                p1 += 1
                p2 += 1
            if p1 >= len(s):
                return True
        
        return p1 == len(s) 