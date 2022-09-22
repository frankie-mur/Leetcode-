class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        U- Calculate the happynumber by sum of the square of its digits, repeat this until == 1, if it ends in 1 its happy if not it will loop endlessly. Return if happy number
        M- Simulation? Follow the algorihim. Can use a set to prevent endless loops
        P- Copy the instructions into code, use a seen set to check for a loop 
        I- coded in python 
        R- code seems to run fine, cant think of any edge cases
        E- Time: O(logn) with n being how many times to sum to 1 or loop 
            Space: O(n) from the set
        '''
        
        seen = set()
        cur = 0
        while True:
            while n:
                cur += (n%10) ** 2
                n = n // 10
            if cur in seen:
                return False
        
            if cur == 1:
                return True
            seen.add(cur)
            n = cur
            cur = 0
        
        return -1
            
        
            
            
            
            
            
            
        
        
            
    

        
        
            