class Solution:
    def climbStairs(self, n: int) -> int:
        #fibo
        a = 1
        b = 0
        ttl = a + b
        while n > 0:
            a = b
            b = ttl
            ttl = a + b
            n-=1
        
        return ttl
        
        
        
        
        
        
        '''
        n = 5
        
        
        
        
        
        
        '''