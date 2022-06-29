class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = dict()
        for i,num in enumerate(nums):
            dif = target - num
            if dif in hm:
                return [i, hm[dif]]
            else:
                hm[num] = i
            
        return -1
        