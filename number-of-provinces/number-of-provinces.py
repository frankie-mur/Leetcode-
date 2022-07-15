class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.n = len(isConnected)
        parents = [i for i in range(self.n)]
        depth = [1] * self.n
        
        def find(x):
            while parents[x] != x:
                x = find(parents[x])
            return x
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            
            if rootX != rootY:
                if depth[rootX] > depth[rootY ]:
                    parents[rootY] = rootX
                elif depth[rootX] < depth[rootY]:
                    parents[rootX] = rootY
                else:
                    parents[rootX] = rootY
                    depth[rootX] += 1
        
                self.n-=1
        
        
        for parent in range(len(isConnected)):
            for child in range(len(isConnected)):
                print(parent,child)
                if parent == child:
                    continue
                if isConnected[parent][child] == 1:
                    union(parent,child)
                

        return self.n
        
        
                
            