class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = ''
        for num in digits:
            nums += str(num)
        
        plusone = int(nums) + 1
        #print(plusone, num)
        res = []
        for ch in str(plusone):
            res.append(int(ch))
        
        return res