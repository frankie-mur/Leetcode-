class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = dict()
        
        for i,num in enumerate(nums):
            dif = target - num
            
            if dif in dic:
                return [i, dic[dif]]
            
            dic[num] = i
        
        return [-1,-1]
  