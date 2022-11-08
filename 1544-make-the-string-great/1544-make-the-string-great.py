class Solution:
    def makeGood(self, s: str) -> str:
        s = list(s)
        i = 0
        while i < len(s):
            if  i < len(s) - 1 and s[i].lower() == s[i + 1].lower():
                if s[i] != s[i+1]:
                    s.pop(i)
                    s.pop(i)
                    i = 0
                    continue
            i += 1
        
        return ''.join(s)
                
                    
        