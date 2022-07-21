class Solution:
    def firstUniqChar(self, s: str) -> int:
        #two pass one dic storing freq
        freq = collections.Counter(s)
        
        for i, ch in enumerate(s):
            if freq[ch] == 1:
                return i
        
        return -1