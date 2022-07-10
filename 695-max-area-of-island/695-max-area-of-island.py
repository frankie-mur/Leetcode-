class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        scan through the grid when we find a 1 we do dfs lookng for connecting ones in 4 dir,
        keep a global max counter counting the area
        '''
        max_area = 0
     
        def dfs(r,c):
            #counts the first 1
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
                    return 0
            #mark as visited
            grid[r][c] = 0
            print(r,c)
            return 1 + dfs(r-1,c) + dfs(r+1,c) + dfs(r,c-1) + dfs(r,c+1)
        
        max_area = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    max_area = max(dfs(r,c), max_area)
                    
                    
        return max_area
                
                    
    
                
                
        
        