class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        '''
        U - return a running sum of the given array, running sum is res[i] = sum(nums[0]...nums[i])
        ex) [1,2,3,4]
          -> [1,1+2 = 3,1+2+3 = 6, 1+2+3+4 = 10]
        M - simulation? also thinking of summation formula but not sure would work here 
        
        P - have a global current sum and scan thorugh nums appending the current sum with that index included 
        
        I - (coded below)
        
        R - 
            [1,2,3,4]
            runnung_sum = 0
            res = []
            r_s = 1
            res = [1]
            r_s = 3
            res = [1,3]
            r_s = 6
            res = [1,3,6]
            r_s = 10
            res = [1,3,6,10] (looks good)
        
        E - Time: O(n) for looping through nums
            Space: O(n) for running sum and resulting list
        
        Can we do better?
        
        '''
        
        running_sum, = 0, 
        
        for i, num in enumerate(nums):
            running_sum += num
            nums[i] = running_sum
        
        return nums