class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a = 0
        b = cost[0]
        
        for i in range(1, len(cost)):
            a, b = b, min(a + cost[i], b + cost[i])
        
        return min(a, b)
        