class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #solve using disjount sets
        if len(edges) != n-1:
            return False
    
        parents = [i for i in range(n)]
        rank = [1] * n
        
        def find(x):
            while parents[x] != x:
                x = find(parents[x])
            return x
        
        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parents[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parents[rootX] = rootY
                else:
                    parents[rootY] = rootX
                    rank[rootX] += 1
                    
                
        
                
        for u, v in edges:
            union(u, v)
            
        
        return len({find(i) for i in range(n)}) == 1
        
        
        
        
            
            
        
        
            
            
            
    
        
        