class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        #UF
        parents = [i for i in range(26)]
        
        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            x = find(x)
            y = find(y)
            
            parents[y] = x
        
        
        for eq in equations:
            v1, v2, op = eq[0], eq[3], eq[1]
            if op == "!":
                continue
            v1 = ord(v1) - ord('a')
            v2 = ord(v2) - ord('a')
            
            union(v1, v2)
        
        for eq in equations:
            v1, v2, op = eq[0], eq[3], eq[1]
            if op == "=":
                continue
                
            v1 = ord(v1) - ord('a')
            v2 = ord(v2) - ord('a')
        
            if find(v1) == find(v2):
                return False
    
        return True