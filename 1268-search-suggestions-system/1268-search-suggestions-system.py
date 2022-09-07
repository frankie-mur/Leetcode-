class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []
        self.n = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.cur = self.root
    
    def add_word(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            
            cur = cur.children[ch]
            
            if cur.n < 3:
                cur.suggestions.append(word)
                cur.n += 1
    
    def search_prefix(self, ch):
        #we want to go to the end of the prefix
        if self.cur and ch in self.cur.children:
            self.cur = self.cur.children[ch]
            return self.cur.suggestions
        else:
            self.cur = []
            return ''
        
    
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = Trie()
        res = []
        
        for word in sorted(products):
            root.add_word(word)
        s = ""
        
        return [root.search_prefix(ch) for ch in searchWord]
        
        
        

        
        
        
                    
                    
            