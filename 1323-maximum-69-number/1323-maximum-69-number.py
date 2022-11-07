class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        num = [num for num in num]
        
        for i, n in enumerate(num):
            if n == "6":
                num[i] = "9"
                break
        
        return "".join([n for n in num])
                