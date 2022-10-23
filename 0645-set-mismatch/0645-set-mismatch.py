class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set(nums)
        res = []
        res.extend([key for key,val in Counter(nums).items() if val == 2])
        for i in range(len(nums)):
            if i + 1 not in seen:
                res.append(i + 1)
                break
        
        return res
            
        
        