class Solution:
    def canJump(self, nums):
        goal_post = len(nums) - 1
        n = len(nums)
        for i in range(n - 1, -1, -1):
            if i + nums[i] >= goal_post:
                goal_post = i
        
        return not goal_post
        
        
        