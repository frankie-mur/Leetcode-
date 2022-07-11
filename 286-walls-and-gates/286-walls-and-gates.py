class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        #multi source bfs? If we start at the locations of each gate when we reach an empy room than thatll be its closest gate if all start at the same time..i think
        R, C = len(rooms), len(rooms[0])
        INF = 2**31 - 1
        q = deque([])
        #find out gates
        for r in range(R):
            for c in range(C):
                if rooms[r][c] == 0:
                    q.append((r,c, 1))
        
        #now start bfs on each gate
        while q:
            for _ in range(len(q)):
                r,c, distance = q.popleft()
                
                for dr, dc in [(-1,0), (0, -1), (1, 0), (0, 1)]:
                    row, col = r + dr, c + dc
                    if row < 0 or row == R or col < 0 or col == C or rooms[row][col] != INF:
                        continue
                    #set the current set to the distance from gate
                    rooms[row][col] = distance
                    #keep track of distance from gate
                    q.append((row,col, distance + 1))








