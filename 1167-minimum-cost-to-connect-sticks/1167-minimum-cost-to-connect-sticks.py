class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        #min heap each stick
        if len(sticks) <= 1:
            return 0
        heap = sticks
        heapq.heapify(heap)
        cost = 0
        while len(heap) > 1:
            stick1 = heapq.heappop(heap)
            stick2 = heapq.heappop(heap)
            merge = stick1 + stick2
            cost += merge
            heapq.heappush(heap, merge)
        
        return cost
            
            
        