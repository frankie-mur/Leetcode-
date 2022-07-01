class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-stones[num] for num in range(len(stones))]
        heapify(pq)
        
        while len(pq) > 1:
            y,x = -heappop(pq), -heappop(pq)
            
            if x == y:
                continue
            
            else:
                heappush(pq,-(y - x))
        if len(pq) == 0:
            return 0
        return -heappop(pq)
        