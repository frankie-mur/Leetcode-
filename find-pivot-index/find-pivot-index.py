class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''
        [0,1,8,11,17,22,28]
                   
        '''
        ttlleft, ttlright = 0, sum(nums)
        
        for i, cur_sum in enumerate(nums):
            ttlright -= cur_sum
            
            if ttlleft == ttlright:
                return i
            
            ttlleft += cur_sum
        
        return -1