"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':  
        if not root:
            return root
        
#         def set_pointers(node_list):
#             for i in range(len(node_list) - 1):
#                 node_list[i].next = node_list[i+1]
            
#             node_list[len(node_list)-1].next = None
        
        q = deque([root])
        
        while q:
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                
                if i < size - 1:
                    cur.next = q[0]
                
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
     
        
        return root
        
            
                