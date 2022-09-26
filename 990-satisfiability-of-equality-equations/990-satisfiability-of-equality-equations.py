class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        #union find!
        parents = [i for i in range(26)]
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            
            return parents[x]
        
        def union(x, y):
            a = find(x)
            b = find(y)
            
            parents[a] = b
        
        for eq in equations:
            v1, v2, op = eq[0], eq[3], eq[1]
            if op == "!":
                continue
            
            a = ord(v1) - ord('a')
            b = ord(v2) - ord('a')
            
            union(a,b)
        
        for eq in equations:
            v1, v2, op = eq[0], eq[3], eq[1]
            if op == "=":
                continue
            
            a = ord(v1) - ord('a')
            b = ord(v2) - ord('a')
            
            if find(a) == find(b):
                return False
        
        return True
            
            
            
            
            
            
        