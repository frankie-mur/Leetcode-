class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        pq = [num for num in nums]
        heapify(pq)
        
        res = 0
        count = 0
        prev = None
        while pq:
            num = heappop(pq)
            if prev is not None and (num == prev + 1 and prev != num):
                count += 1
                res = max(res, count)
            elif prev == num:
                continue
            else:
                count = 0
            prev = num
        
        return res + 1
        
            
        
            
        
        