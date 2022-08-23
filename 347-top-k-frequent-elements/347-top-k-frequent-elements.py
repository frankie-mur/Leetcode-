class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        heap = []
        
        for key,val in freq.items():
            heapq.heappush(heap, (-val,key))
            
        res = []
        
        while k:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        
        return res
        
                
                

    
        
        
        