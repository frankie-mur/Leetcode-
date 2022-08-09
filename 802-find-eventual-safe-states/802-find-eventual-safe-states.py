class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        #if node has a cycle it cannot be safe
        status = [0] * len(graph)

        
        def is_cycle(node):
            if status[node] == 'visited':
                return True
            if status[node] == 'safe':
                return False
            
            status[node] = 'visited'
            
            for nei in graph[node]:
                if is_cycle(nei):
                    return True
            
            status[node] = 'safe'
            return False
                    
        
        res = []
        for node in range(len(graph)):
            if not is_cycle(node):
                res.append(node)
        
        return res
    
    

            
                    
                
            
            