class Solution:
    def isHappy(self, n: int) -> bool:
        def square_sum(num):
            total = 0
            while num:
                total += (num % 10) ** 2
                num = num // 10
            return total
        
        
        seen = set()
        
        while n != 1:
            new_num = square_sum(n)
            if new_num in seen:
                return False
            seen.add(new_num)
            n = new_num
        
        return True if n == 1 else False