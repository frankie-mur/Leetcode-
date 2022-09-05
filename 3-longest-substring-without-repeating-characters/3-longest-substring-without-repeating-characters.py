class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l, r = 0, 0
        n = len(s)
        longest = 0
        while r < n:
            rch = s[r]
            if rch not in seen:
                seen.add(rch)
                longest = max(longest, (r - l) + 1)
                r += 1
            else:
                lch = s[l]
                seen.remove(lch)
                l += 1
        
        return longest
                
                