class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        dicS = defaultdict(list)
        for idx,ch in enumerate(s):
            dicS[ch].append(idx)
        
        def check(string):
            idx = -1
            
            for ch in string:
                idx = s.find(ch, idx+1)
                
                if idx == -1:
                    return False
            
            return True
            
        
        res = 0
        for word in words:
            if check(word):
                res += 1
        
        return res