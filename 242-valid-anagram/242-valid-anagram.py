class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = dict()
        
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        
        for ch in t:
            if ch in freq:
                freq[ch] -= 1
                if freq[ch] == 0:
                    del freq[ch]
        
        return len(freq) == 0
        