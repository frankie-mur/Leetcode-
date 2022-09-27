class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        
        for tup in zip(*strs):
            if len(set(tup)) > 1:
                break
            res += tup[0]
        
        return res