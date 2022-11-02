class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cur = ''
        
        for chs in zip(*strs):
            if len(set(chs)) == 1:
                cur += chs[0]
            else:
                break
        
        return cur