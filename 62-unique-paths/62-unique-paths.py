class Solution:
    def uniquePaths(self, m, n):
        memo = {}
        
        def dp(r,c):
            if r == 1 and c == 1:
                return 1
            if r == 0 or c == 0:
                return 0
            
            if (r,c) not in memo:
                memo[(r,c)] = dp(r-1,c) + dp(r, c-1)
            
            return memo[(r,c)]
        
        return dp(m,n)
        
        
        
        
        
        