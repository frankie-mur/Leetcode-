class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        key point: distant number in range [0,n]? Cyclic Sort!
        loop through the array and plave each number at its correct index if there isnt a match that is the solution?
        ex:
        [2,0,1]
        length = 3
        make sure everynumber between 0,3 is in there if not return that num
        '''
        
        length, i = len(nums), 0
        
        #cylic sort
        while i < length:
            j = nums[i]
            if j < length and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
            
        
        #linear scan of missing num
        for i, num in enumerate(nums):
            if num != i:
                return i
        
        return length
                
                
            
        
        