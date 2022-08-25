class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        U - Find the longest common prefix among an array of strings
        M - Pointers all across?, or use cool zip pattern
        P - 
        
        '''
        

        pre = strs[0]
        for i in strs:
            while not i.startswith(pre):
                pre = pre[:-1]
            
        return pre     