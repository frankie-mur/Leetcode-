class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []                      
        res = []
        nums.sort()
        
        def find_target(num, idx):
            l = idx + 1
            r = len(nums) - 1
            
            while l < r:
                three_sum = num + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([num,nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                        
        
        for idx,num in enumerate(nums):
            #duplicate
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            
            find_target(num, idx)
        
        
        return res