"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        q = deque([root])
        level_order = []
        
        while q:
            size = len(q)
            cur_lvl = []
            for i in range(size):
                cur = q.popleft()
                cur_lvl.append(cur.val)
            
                for nei in cur.children:
                    q.append(nei)
                
                if i == size - 1:
                    level_order.append(cur_lvl)
        
        return level_order
            
            
        
        