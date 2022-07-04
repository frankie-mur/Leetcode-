import collections

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        ''' DFS through tree coloring each vertex, if there is a color conflict return false'''
        colors = {}
        
        for vertex in range(len(graph)):
            if vertex in colors:
                continue
                
            stack = [vertex]
            colors[vertex] = 1
            
            while stack:
                cur = stack.pop()
                for nei in graph[cur]:
                    if nei in colors:
                        if colors[nei] == colors[cur]:
                            return False
                    else:
                        stack.append(nei)
                        colors[nei] = colors[cur] * -1 
            
        return True
                
                        
                
                
        
                        
            
            
            
        
        
        
        