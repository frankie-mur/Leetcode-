class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = defaultdict(int)
        prefix[0] = -1
        running = 0
        
        for idx, num in enumerate(nums):
            running += num
            rem = running % k
            
            if rem not in prefix:
                prefix[rem] = idx
            elif idx - prefix[rem] >= 2:
                return True
        
            
        return False
            
            
        
        
        
            
            