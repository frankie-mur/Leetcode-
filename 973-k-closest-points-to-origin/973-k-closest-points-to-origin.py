class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        def dist_to_origin(x,y) -> int:
            return math.sqrt((x -0 )** 2 + (y - 0) ** 2)
        
        for x,y in points:
            dist = dist_to_origin(x,y)
            heapq.heappush(heap, (-dist, [x,y]))
            
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        
        return res
        
            