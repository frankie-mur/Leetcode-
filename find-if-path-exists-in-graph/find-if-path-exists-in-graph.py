class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #create adj_list
        adj_list = defaultdict(list)
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        def dfs(adj_list, node, destination,visited):
            if node == destination:
                return True
            if node not in visited:
                visited.add(node)
                for neig in adj_list[node]:
                    res = dfs(adj_list, neig, destination,visited)
                    if res: return True
            return False
        
        return dfs(adj_list, source, destination,set())
        
                    
                    
                
                    
            