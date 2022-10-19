class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        #heap space optimized
        
        
        heap = []
        freq = Counter(words)
        
        for word, count in freq.items():
            heapq.heappush(heap, (-count, word))
        
#             if len(heap) > k:
#                 heapq.heappop(heap)
        
        res = []
        
        while k:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        
        return res
        
        
        
            