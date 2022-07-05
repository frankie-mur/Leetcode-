class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res, seen = 0, set(nums)
        
        for num in nums:
            if num - 1 not in seen:
                #we can start looking for consecutive
                temp = 0
                counter = num
                while counter in seen:
                    temp += 1
                    counter += 1
                
                res = max(res, temp)
        
        return res
        
        
        
        
        
        '''
        #this uses a heap and is nlogn
        if not nums:
            return 0
        pq = [num for num in nums]
        heapify(pq)
        
        res = 0
        count = 0
        prev = None
        while pq:
            num = heappop(pq)
            if prev is not None and num == prev + 1:
                count += 1
                res = max(res, count)
            elif prev == num:
                continue
            else:
                count = 0
            prev = num
        
        return res + 1
        '''
            
        
            
        
        