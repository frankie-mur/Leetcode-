class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        awesome solution here, implements vertical scanning using the zip method. We use * to unpack 
        and the set to make sure they are all the same chars.
        
        '''
        res = ''
        for ch in zip(*strs):
            if len(set(ch)) != 1:
                break
            res += ch[0]
        
        return res
        