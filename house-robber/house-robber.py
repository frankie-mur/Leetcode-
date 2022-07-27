class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        
        def dp(idx):
            if idx == 0:
                return nums[0]
            if idx == 1:
                return max(nums[0], nums[1])
            if idx not in memo:
                memo[idx] = max(dp(idx-1), dp(idx-2) + nums[idx])
                
            return memo[idx]
        
        return dp(len(nums) - 1)
        
            
         
        
        