class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        '''
        U- given a cake size h x w and two arrays of intergers that represent horizantal and vertical cuts, return the max area of a piece of cake after the cuts are preformed
        M- Simulation? Array? Greedy.
        P- Sort both given arrays, compute the maximum difference between two consecutive elements in each array. Make sure to take array bounds into account
        I- python
        R - I think it passes all test casses, trying to think how to refactor to one loop
        E - 
        '''
        horizontalCuts.sort()
        verticalCuts.sort()
        max_horizontal, max_vertical = 0,0
        for i in range(len(horizontalCuts)):
            if i == 0:
                max_horizontal = max(max_horizontal, abs(horizontalCuts[i] - 0))
            if i == len(horizontalCuts) - 1:
                max_horizontal = max(max_horizontal, abs(horizontalCuts[i] - h))
            if i < len(horizontalCuts)-1:
                max_horizontal = max(max_horizontal, abs(horizontalCuts[i+1] - horizontalCuts[i]))     
            
        for i in range(len(verticalCuts)):
            if i == 0:
                max_vertical = max(max_vertical, abs(verticalCuts[i] - 0))
            if i == len(verticalCuts) - 1:
                max_vertical = max(max_vertical, abs(verticalCuts[i] - w))
            if i < len(verticalCuts)-1:
                max_vertical = max(max_vertical, abs(verticalCuts[i+1] - verticalCuts[i]))     
      
        return (max_horizontal * max_vertical) % (10**9 + 7)
                
                                     
        
                        
                                    
            
        
                                
                
            
        