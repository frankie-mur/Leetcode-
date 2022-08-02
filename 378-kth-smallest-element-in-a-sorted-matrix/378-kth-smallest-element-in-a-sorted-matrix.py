class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for row in matrix:
            heap.extend(row)
        
        heapq.heapify(heap)
        while k >  1:
            k -= 1
            heapq.heappop(heap)
        
        return heapq.heappop(heap)