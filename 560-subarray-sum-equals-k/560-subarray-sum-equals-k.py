class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        cur_sum = 0
        res = 0
        for num in nums:
            cur_sum += num
            #left to right
            if cur_sum == k:
                res += 1
            
            target = cur_sum - k
            res += prefix[target]
            prefix[cur_sum] += 1
        
        return res
            
        