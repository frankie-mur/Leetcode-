U: Given array room, each room contains keys to other room. We can only enter a room with       its key. Return if we can visit all rooms.
M: Graph problem, each room represents a vertex and the keys are its edges.
P:
Iterative dfs with stack
visited set
start at room 0, add to visited then loop through its keys. Add these to visited, in        the end we could return if the set is the length of rooms
I:python
R: rooms = [[1],[2],[3],[]]
stack =        vertex = 3
visited = 0,1,2,3
returns True