class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #create adj_list
        adj_list = defaultdict(list)
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            
        q = deque([source])
        visited = set([source])
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == destination:
                    return True
                
                for nei in adj_list[cur]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
                
        return False
                    
        
                
            
            
            
            
                
                    
            
        
        
        
                    
                    
                
                    
            