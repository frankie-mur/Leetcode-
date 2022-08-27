class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = collections.Counter(magazine)
        
        for ch in ransomNote:
            freq[ch] -= 1
            if freq[ch] < 0:
                return False
        
        return True
                