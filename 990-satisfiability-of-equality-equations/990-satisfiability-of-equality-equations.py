class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        #uf
        parents = [i for i in range(26)]
        
        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            x = find(x)
            y = find(y)
            
            parents[x] = y
        
        
        for eq in equations:
            v1, v2, op = eq[0], eq[3], eq[1]
            if op == "=":
                a = ord(v1) - ord('a')
                b = ord(v2) - ord('a')
                
                union(a, b)
        
        for eq in equations:
            v1, v2, op = eq[0], eq[3], eq[1]
            if op == "!":
                a = ord(v1) - ord('a')
                b = ord(v2) - ord('a')
                
                if find(a) == find(b):
                    return False
        
        return True
            
            