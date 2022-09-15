class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        
        def find_target(idx, num):
            l = idx + 1
            r = n - 1
            
            while l < r:
                three_sum = nums[idx] + nums[l] + nums[r]
                if three_sum == 0:
                    #result
                    res.append([nums[idx], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif three_sum > 0:
                    r -= 1
                else:  
                    l += 1
        
        
        
        for idx, num in enumerate(nums):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            find_target(idx, num)
        
        return res