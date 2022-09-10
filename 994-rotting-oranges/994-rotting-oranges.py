class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque([])
        R, C = len(grid), len(grid[0])
        minutes = 0
        DIRS = [(-1,0), (0,-1), (1,0), (0,1)]
        fresh = 0
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    rotten.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        def is_valid(r,c):
            if 0 <= c < C and 0 <= r < R and grid[r][c] == 1:
                return True
            return False
        
        
        while rotten and fresh:
            size = len(rotten)
            for _ in range(size):
                r,c = rotten.popleft()
                #print(r,c, minutes)
                for dr,dc in DIRS:
                    if is_valid(r + dr, c + dc):
                        grid[r + dr][c + dc] = 2
                        fresh -= 1
                        rotten.append((r + dr, c + dc))
                
            minutes += 1
    
        if fresh == 0:
            return minutes
        return -1
        





