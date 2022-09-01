class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #multisource bfs
        #first find all the rotten oranges
        R, C = len(grid), len(grid[0])
        origin = deque()
        fresh = 0
        minutes = 0
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    origin.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        DIRS = [(-1,0), (0,-1), (1, 0), (0, 1)]
        
        def is_valid(r, c):
            if c >= 0 and c < C and r >= 0 and r < R and grid[r][c] == 1:
                return True
            return False
        
        while origin and fresh > 0:
            size = len(origin)
            for _ in range(size):
                r, c = origin.popleft()
                
                for dr, dc in DIRS:
                    newr, newc = r + dr, c + dc
                    if is_valid(newr, newc):
                        grid[newr][newc] = 2
                        origin.append((newr, newc))
                        fresh -= 1
                
            minutes += 1
                        
                
                
        return minutes if fresh == 0 else -1
        
        