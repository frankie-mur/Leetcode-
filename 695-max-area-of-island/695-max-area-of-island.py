class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        scan through the grid when we find a 1 we do dfs lookng for connecting ones in 4 dir,
        keep a global max counter counting the area
        '''
        
        R, C = len(grid), len(grid[0])
        max_area = 0
        self.cur_area = 0
        
        def dfs(r,c):
            #mark as visited
            grid[r][c] = 0
            self.cur_area += 1
            #traverse all 4 directions
            for dr,dc in [(-1,0), (0,-1), (1,0), (0,1)]:
                row,col = r + dr, c + dc
                if row < 0 or row == R or col < 0 or col == C or grid[row][col] == 0:
                    continue
                dfs(row, col)
        
        
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    self.cur_area = 0
                    dfs(r,c)
                    max_area = max(max_area, self.cur_area)
                 
        
        return max_area
                    
        

                
                
        
        