class LLNode:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        #key: key, val: pointer to the node in the LL
        self.cache = {}
        self.MRU = LLNode()
        self.LRU = LLNode()
        #now connect them
        self.MRU.prev = self.LRU
        self.LRU.next = self.MRU
        
    def get(self, key: int) -> int:
        if key in self.cache:
            #update the node bc we just used it 
            node = self.cache[key]
            self.delete(node)
            self.insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            #delete and update value
            self.delete(self.cache[key])    
        self.cache[key] = LLNode(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            lru = self.LRU.next
            self.delete(lru)
            del self.cache[lru.key]
    
    def insert(self, node: LLNode):
        #insert inbetween MRU and LRU
        prev, nxt = self.MRU.prev, self.MRU
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev
    
    def delete(self, node: LLNode):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)