class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        '''
        Make a unique pattern list for each ch
        ex) 'abb' = [0, 1, 1]
            'aqq' = [0 , 1, 1]
            
        '''
        def helper(word):
            count, uniq = 0, defaultdict()
            res = []
            for ch in word:
                if ch not in uniq:
                    uniq[ch] = count
                    count += 1
            
                res.append(uniq[ch])
            
            return res
                
        pattern_uniq = helper(pattern)    
        
        return [word for word in words if helper(word) == pattern_uniq]
        
                    
                    
                    
        
                