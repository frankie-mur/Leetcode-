class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set()
        for letter in brokenLetters:
            broken.add(letter)
        
        words = text.split(" ")
        typed_words = 0
        for word in words:
            found = False
            for ch in word:
                if ch in broken:
                    found = True
                    break
            
            if not found:                    
                typed_words += 1
        
        
        return typed_words
            
                
        
        
        
            
        
        
            
            
        
        