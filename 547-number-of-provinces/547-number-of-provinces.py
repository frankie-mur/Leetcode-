class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(node, visited):
            for idx, node in enumerate(isConnected[node]):
                if node == 1 and idx not in visited:
                    visited.add(idx)
                    dfs(idx, visited)
        
        
        n = len(isConnected)
        visited = set()
        count = 0
        
        
        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node, visited)
                count += 1
        
        return count
                