class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        start, end = 0,0
        while end < len(prices):            
            if prices[start] > prices[end]:
                start = end
            else:
                maxP = max(maxP, prices[end] - prices[start])
                end += 1

        return maxP
        
        
        
            
 