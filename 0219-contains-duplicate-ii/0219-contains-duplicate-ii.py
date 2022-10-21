class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        w_start = 0
        for w_end in range(len(nums)):
            if nums[w_end] in seen:
                return True
            seen.add(nums[w_end])
            if w_end - w_start + 1 > k:
                seen.remove(nums[w_start])
                w_start += 1
        
        return False
    
    
    
    '''
    
    nums = [1,2,3,1,2,3], k = 2
              s    
                e 
        
        seen = 2, 3
    
    '''
    
    
            