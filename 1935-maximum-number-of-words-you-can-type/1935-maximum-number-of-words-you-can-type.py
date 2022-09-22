class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)    
        words = text.split(" ")
        typed_words = len(words)
        
        for word in words:
            found = False
            for ch in word:
                if ch in broken:
                    typed_words -= 1
                    break

        return typed_words
            
                
        
        
        
            
        
        
            
            
        
        