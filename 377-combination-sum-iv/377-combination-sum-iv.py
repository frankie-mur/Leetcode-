class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        cache = [None] * (target+1)
        has_cache = [False] * (target+1)
        
        def get_count(target):
            if target == 0:
                return 1
            if target < 0:
                return 0
            
            if has_cache[target]:
                return cache[target]
            
            has_cache[target] = True
            
            res = 0  
            for x in nums:
                if target >= x:
                    res += get_count(target-x)
        
            cache[target] = res
            return res
        
        return get_count(target)