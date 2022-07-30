class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        mx = defaultdict(int)
        
        for word in words2:
            c = collections.Counter(word)
            
            for key in c:
                mx[key] = max(mx[key], c[key])
        
        res = []
        
        for word in words1:
            c = collections.Counter(word)
            found = True
            for key in mx:
                if c[key] < mx[key]:
                    found = False
                
            
            if found:
                res.append(word)
                    
        return res    
        
        
        