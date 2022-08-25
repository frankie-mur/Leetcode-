class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        U - Find the longest common prefix among an array of strings
        M - Pointers all across?, or use cool zip pattern
        P - 
        
        '''
        
        res = ""
        
        for ch in zip(*strs):
            if len(set(ch)) > 1:
                break
            res += ch[0]
        
        return res