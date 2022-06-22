class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        mh = []
        heapify(mh)

        for num in nums:
            heappush(mh, -1 * num)
            
            #if len(mh) > k:
            #    heappop(mh)
        
        while k > 1:
            heappop(mh)
            k -= 1
        
        return -1 * heappop(mh)
        
        
        
        