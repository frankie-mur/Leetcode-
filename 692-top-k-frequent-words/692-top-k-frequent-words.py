class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}
        for word in words:
            freq[word] = freq.get(word,0) + 1
        heap = [(-val,key) for key,val in freq.items()]
        
        heapify(heap)
        
        return [heappop(heap)[1] for _ in range(k)]
        