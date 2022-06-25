# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(root, p, q):
            if not root:
                return
            
            parent_val = root.val
            if p.val < parent_val and q.val < parent_val:
                #search on left
                return dfs(root.left, p, q)
            elif p.val > parent_val and q.val > parent_val:
                #search on right
                return dfs(root.right, p, q)
            else:
                return root
        
        return dfs(root,p,q)