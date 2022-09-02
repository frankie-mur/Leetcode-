class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def is_valid(r:int,c:int) -> bool:
            if c >= 0 and c < C and r >= 0 and r < R and grid[r][c] == 1:
                return True
            return False
        
        
        R, C = len(grid), len(grid[0])
        rotten = deque([])
        DIRS = [(-1,0), (0,-1), (1,0), (0,1)]
        fresh, minutes = 0, 0
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rotten.append((r,c))
        
        
        while rotten and fresh:
            size = len(rotten)
            for _ in range(size):
                r, c = rotten.popleft()
                print(r,c)
                for dr, dc in DIRS:
                    newr, newc = r + dr, c + dc
                    if is_valid(newr, newc):
                        fresh -= 1
                        grid[newr][newc] = 2
                        rotten.append((newr, newc))
            
            minutes += 1
        
        return minutes if fresh == 0 else -1
            
            
            
        
        