class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:       
        stack = [0]
        visited = set([0])
        while stack:
            vertex = stack.pop()

            for nei in rooms[vertex]:
                if nei not in visited:
                    visited.add(nei)
                    stack.append(nei)

        return len(visited) == len(rooms)
        
