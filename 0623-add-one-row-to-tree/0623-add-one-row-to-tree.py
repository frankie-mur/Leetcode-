# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        #bfs get the row before depth
        if depth == 1:
            return TreeNode(val=val,left=root)
        
        
        q = deque([root])
        
        cur_row = []
        while q:
            size = len(q)
            cur_row = []
            for _ in range(size):
                cur = q.popleft()
                cur_row.append(cur)
                
                
                if cur.left:
                    q.append(cur.left)
                    
                if cur.right:
                    q.append(cur.right)
            
            depth -= 1
            if depth == 1:
                break
        
        for node in cur_row:
            node.left = TreeNode(val, left = node.left)
            node.right = TreeNode(val, right = node.right)
        
        return root
                
                
                    