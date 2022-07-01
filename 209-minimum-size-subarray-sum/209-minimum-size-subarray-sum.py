class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        w_start, cur_sum, min_sum = 0,0,math.inf
        for w_end in range(len(nums)):
            cur_sum += nums[w_end]
            while cur_sum >= target:
                min_sum = min(min_sum, w_end - w_start + 1)
                cur_sum -= nums[w_start]
                w_start += 1
        
        if min_sum == math.inf:
            return 0
        return min_sum
            