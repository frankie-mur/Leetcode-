class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        
        min_str = min([len(s) for s in strs])
        start = strs[0]
        
        for idx in range(min_str):
            for s in strs:
                if start[idx] != s[idx]:
                    return res
            
            res += start[idx]
        
        return res
                


            

        

            
        