class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R,C = len(grid), len(grid[0])
        def dfs(r,c):
            def is_land(new_r,new_c):
                if new_r >= 0 and new_r < R and new_c >= 0 and new_c < C and grid[new_r][new_c] == '1':
                    return True
                return False
                
            grid[r][c] = 0
            for dr,dc in ([(-1,0),(0,-1),(1,0), (0,1)]):
                new_r,new_c = r + dr, c + dc
                if is_land(new_r,new_c):
                    dfs(new_r, new_c)
        
        islands = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    dfs(r,c)
                    islands += 1
        
        return islands
                    

            
             