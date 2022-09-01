class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = collections.Counter(magazine)
        
        for ch in ransomNote:
            if ch in freq:
                freq[ch] -= 1
                if freq[ch] < 0:
                    return False
            else:
                return False
        
        return True