class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #U- given an list and two ints k and x return the k closest ints to x in the array. If distanses are the same between two elements the smallest on wins. The result should also be sorted
        
        #M - ? min Heap
        
        #P - 
        
        
        #[1,2,3,4,5] k = 4, c = 3
        # (2,1), (1,2), (0,3), (1, 4), (2, 5)
        # [1,2,3,4]
        #with this solution we have to sort twice...

        heap = []
        res = []
        
        for num in arr:
            dist = abs(num - x)
            heappush(heap, (dist, num))
            
            #space optimiztion?
            #if len(heap) > k:
            #   heappop(heap)
        
        while k:
            res.append(heappop(heap)[1])
            k -= 1
        
        return sorted(res)
        
        
        
    