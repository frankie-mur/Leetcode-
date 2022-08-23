class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        U - Given stock prices array we want to return the best profit, we must buy on a single day and sell after. 
        M - Two pointer, greedy
        P - We can be gready here, we want to buy low and sell high, therfore if out left pointer is larger than our right we can move our left to our right, 
        we calculate the largest profit as we move along
        I - Python
        R - Passes test casses
        E - Time O(n)
            Space O(1)
        
        '''
        n = len(prices)
        max_profit = 0
        L = 0
        
        for R in range(1, n):
            buy, sell = prices[L], prices[R]
            profit = sell - buy
            if buy > sell:
                L = R
            else:
                max_profit = max(max_profit, profit)
        
        return max_profit 
            
        
        
        
            
 