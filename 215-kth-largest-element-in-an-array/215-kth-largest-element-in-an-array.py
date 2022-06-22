class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        mh = []
        heapify(mh)

        for num in nums:
            heappush(mh, num)
            
            while len(mh) > k:
                heappop(mh)
        
        return heappop(mh)
        
        
        
        