class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        '''
        U-isomorphic..if chars in s can be replaced to get t.Trick here is that only one mapping per char
        M-I think a hashmap can be used for the mappings
        P-First check the lengths, if not same False. No loop through each char in strings, if not equal than
        check if a mapping already, if there is than check if its equal to the not equal in t, else create the mapping
        I- python
        R- 
        E- Time: O(n)
            Space: O(n)
        '''
        if len(s) != len(t):
            return False
        
        dicST, dicTS = {}, {}
        for i in range(len(s)):
            c1,c2 = s[i], t[i]
            if ((c1 in dicST and dicST[c1] != c2) or (c2 in dicTS and dicTS[c2] != c1)):
                return False
            dicST[c1] = c2
            dicTS[c2] = c1
        
        return True
        
        