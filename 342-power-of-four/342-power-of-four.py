class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n > 1 and n % 4 == 0:
            n =  n // 4
        
        return n == 1
        