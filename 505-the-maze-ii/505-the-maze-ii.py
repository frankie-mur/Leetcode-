class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
    #dijstras
        R, C = len(maze), len(maze[0])
        heap = [(0, start)]
        visited = set()
        DIRS = [(-1,0), (0,-1), (1,0), (0,1)]
        
        def roll(r, c, dr, dc, dist):
            while 0 <= r + dr < R and 0 <= c + dc < C and maze[r + dr][c + dc] == 0:
                r += dr
                c += dc
                dist += 1
            
            return r, c, dist

        while heap:
            dist, location = heapq.heappop(heap)
            r, c = location
            
            if [r,c] == destination:
                return dist
            
            visited.add((r,c))
            
        
            for dr, dc in DIRS:
                newr , newc, new_dist = roll(r, c, dr, dc, dist)
                
                if (newr, newc) not in visited:
                    heapq.heappush(heap, (new_dist, (newr,newc)))
                    
        
        return -1
                
            
            