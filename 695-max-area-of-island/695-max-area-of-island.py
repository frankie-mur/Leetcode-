class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        scan through the grid when we find a 1 we do dfs lookng for connecting ones in 4 dir,
        keep a global max counter counting the area
        '''
        max_area = 0
        visited = set()
        cur_area = 0
        def dfs(r,c):
            #counts the first 1
            nonlocal cur_area
            cur_area += 1
            nonlocal max_area
            max_area = max(cur_area, max_area)
            visited.add((r,c))
            for new_r,new_c in [(-1,0), (0,-1), (1,0), (0,1)]:
                if r+new_r < 0 or r+new_r >= len(grid) or c+new_c < 0 or c+new_c >= len(grid[0]):
                    continue
                if grid[r+new_r][c+new_c] == 1 and (r+new_r,c+new_c) not in visited:                 
                    dfs(r+new_r,c+new_c)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in visited:
                    cur_area = 0
                    dfs(r,c)
                    
                    
        return max_area
                
                    
    
                
                
        
        