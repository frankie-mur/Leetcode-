class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #union find
        parents = [i for i in range(n)]
        self.nodes = n
        rank = [1] * n
        
        def find(x):
            while parents[x] != x:
                x = find(parents[x])
            
            return x
        
        def union(x, y):
            rootX, rootY = find(x), find(y)
            
            if parents[rootX] != rootY:
                #union by rank
                if rank[rootX] > rank[rootY]:
                    parents[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parents[rootX] = rootY
                else:
                    parents[rootY] = rootX
                    rank[rootX] += 1
                
                self.nodes -= 1
        
        
        for u,v in edges:
            union(u,v)
        
        
        return self.nodes
        
        
        
        
        