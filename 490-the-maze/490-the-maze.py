class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        #bfs?
        R, C = len(maze), len(maze[0])
        visited = set()
        stack = [start]
        DIRS = [(-1,0), (0,-1), (1,0), (0,1)]
        
        def roll(r, c, dr, dc):
            while 0 <= r+dr < R and 0 <= c+dc < C and maze[r+dr][c+dc] == 0:
                r += dr
                c += dc
            
            return r, c
        
        while stack:
            r, c = stack.pop()
            visited.add((r,c))
            #print(r,c)
            if [r,c] == destination:
                return True
            
            for dr, dc in DIRS:
                newr, newc = roll(r, c, dr, dc)
                #print(newr, newc)
                if (newr, newc) not in visited:
                    # visited.add((newr, newc))
                    stack.append((newr,newc))
        
        
        return False
                
                
                
            
        
        
        