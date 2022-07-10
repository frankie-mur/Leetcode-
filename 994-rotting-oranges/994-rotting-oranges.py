class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #bfs rotten and count 4-dir layers that contain a fresh
        #multi source bfs, first time doint this
        R,C = len(grid), len(grid[0])
        sec, fresh = 0, 0
        q = deque([])
        #first count the number of fresh oranges as well as start q of rotten source oranges
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        
        #now we start the multisource bfs
        while q and fresh > 0:
            size = len(q)
            for _ in range(size):
                r, c = q.popleft()
                
                for dr, dc in [(-1,0), (0, -1), (1, 0), (0, 1)]:
                    #check bounds and if fresh
                    row, col = r + dr, c + dc
                    if row < 0 or row == R or col < 0 or col == C or grid[row][col] != 1:
                        continue
                    #mark rotten
                    grid[row][col] = 2
                    q.append((row, col))
                    fresh -= 1
                
            sec += 1
            
            
        return sec if fresh == 0 else -1 
                
            
            
            
        