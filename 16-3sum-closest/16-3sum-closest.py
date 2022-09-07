class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums: return []                      
        min_closest = math.inf
        nums.sort()
        
        
        def find_target(num, idx):
            l = idx + 1
            r = len(nums) - 1
            
            while l < r:
                three_sum = num + nums[l] + nums[r]
                distance = abs(target-three_sum)
                nonlocal min_closest
                if distance < abs(min_closest):
                    min_closest = target - three_sum
                    
                if three_sum > target:
                    r -= 1
                else:
                    l += 1

                    
        for idx,num in enumerate(nums):            
            find_target(num, idx)
            if min_closest == 0:
                break
        
        
        return target - min_closest