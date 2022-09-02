class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #dfs
        
        visited = set()
        count = 0
        n = len(isConnected)
        
        def dfs(node):
            for idx,node in enumerate(isConnected[node]):
                if node == 1 and idx not in visited:
                    visited.add(idx)
                    dfs(idx)
            
        
        
        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                count += 1
        
        
        return count
        
            
            