# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        q = deque([root])
        zig = False
        while q:
            size = len(q)
            cur_lvl = deque([])
            for _ in range(size):
                cur = q.popleft()
    
                if zig:
                    cur_lvl.appendleft(cur.val)
                else:
                    cur_lvl.append(cur.val)
                
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                
            zig = not zig
            res.append(cur_lvl)
        
        return res
            
            
            
                    