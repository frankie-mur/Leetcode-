class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        key point: distant number in range [0,n]? Cyclic Sort!
        loop through the array and plave each number at its correct index if there isnt a match that is the solution?
        ex:
        [3,0,1]
        length = 3
        make sure everynumber between 0,3 is in there if not return that num
        '''
        
        length = len(nums)
        for num in range(length + 1):
            if num not in nums:
                return num