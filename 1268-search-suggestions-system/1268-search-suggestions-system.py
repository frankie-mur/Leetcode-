class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []
        self.n = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add_word(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            
            cur = cur.children[ch]
            
            if cur.n < 3:
                cur.suggestions.append(word)
                cur.n += 1
    
    def search_prefix(self, prefix):
        #we want to go to the end of the prefix
        cur = self.root
        for ch in prefix:
            if ch not in cur.children:
                return ''
            
            cur = cur.children[ch]
        
        return cur.suggestions
        
    
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = Trie()
        res = []
        
        for word in sorted(products):
            root.add_word(word)
        s = ""
        for ch in searchWord:
            s += ch
            words = root.search_prefix(s)
            res.append(words)
        
        return res
        
        
        

        
        
        
                    
                    
            