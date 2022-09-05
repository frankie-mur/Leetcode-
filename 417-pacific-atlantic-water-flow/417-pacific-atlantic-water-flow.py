class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        pac, atl = set(), set()
        DIRS = [(-1,0), (0, -1), (1, 0), (0 ,1)]
        
        
        def is_valid(r,c, prev, visited):
            if c >= 0 and c < C and r >= 0 and r < R and prev <= heights[r][c] and (r,c) not in visited:
                return True
            return False
        
        def dfs(r,c, visited, prev):
            visited.add((r,c))
            for dr,dc in DIRS:
                if is_valid(r+dr, c+dc, heights[r][c], visited):
                    dfs(r+dr, c+dc, visited, heights[r+dr][c+dc])
        #top and bottom
        for c in range(C):
            dfs(0, c, pac, heights[0][c])
            dfs(R - 1, c, atl, heights[R-1][c])
        
        #left and right
        for r in range(R):
            dfs(r, 0, pac, heights[r][0])
            dfs(r,C-1, atl, heights[r][C-1])
        
        return pac & atl
            
        
        