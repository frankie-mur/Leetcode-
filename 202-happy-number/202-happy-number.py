class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        U- Calculate the happynumber by sum of the square of its digits, repeat this until == 1, if it ends in 1 its happy if not it will loop endlessly. Return if happy number
        M- Simulation? Follow the algorihim. Can use a set to prevent endless loops
        P- Copy the instructions into code, use a seen set to check for a loop 
        I- coded in python 
        R- code seems to run fine, cant think of any edge cases
        E- Time: O(n) with n being how many times to sum to 1 or loop 
            Space: O(n) from the set
        '''
        
        seen = set()
        
        def sum_of_square_digits(n):
            total = 0
            while n:
                total += (n % 10) ** 2
                n = n // 10
            return total
        
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum_of_square_digits(n)
        
        return n == 1
        
            
        
            
            
            
            
            
            
        
        
            
    

        
        
            