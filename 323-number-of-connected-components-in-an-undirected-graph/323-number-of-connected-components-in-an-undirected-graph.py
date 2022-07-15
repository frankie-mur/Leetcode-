class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #union find
        parents = [i for i in range(n)]
        self.nodes = n
        
        def find(x):
            while parents[x] != x:
                x = find(parents[x])
            
            return x
        
        def union(x, y):
            rootX, rootY = find(x), find(y)
            
            if parents[rootX] != rootY:
                self.nodes -= 1
                parents[rootY] = rootX
        
        
        for u,v in edges:
            union(u,v)
        
        
        return self.nodes
        
        
        
        
        