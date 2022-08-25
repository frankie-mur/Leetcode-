class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = collections.Counter(magazine)
        
        for ch in ransomNote:
            if ch not in freq:
                return False
            
            freq[ch] -= 1
            if freq[ch] == 0:
                del freq[ch]
        
        
        return True