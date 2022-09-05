class LinkedList():
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.LRU = LinkedList()
        self.MRU = LinkedList()
        self.LRU.right = self.MRU
        self.MRU.left = self.LRU
        
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.delete(node)
            self.insert(node)
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
        
        self.cache[key] = LinkedList(key, value)
        self.insert(self.cache[key])
    
        if len(self.cache) > self.capacity:
            LRU = self.LRU.right
            self.delete(LRU)
            del self.cache[LRU.key]
    
    def insert(self, node) -> None:
        #insert bewtween MRU and right
        prev, nxt = self.MRU.left, self.MRU
        prev.right = node
        nxt.left = node
        node.left = prev
        node.right = nxt
    
    def delete(self, node) -> None:
        prev = node.left
        nxt = node.right
        prev.right = nxt
        nxt.left = prev
        
    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)