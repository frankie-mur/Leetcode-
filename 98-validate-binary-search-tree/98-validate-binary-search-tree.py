# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #get the values in-order they should all be in asceding order
        vals = []
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            nonlocal vals
            vals.append(root.val)
            dfs(root.right)
        
        dfs(root)
        return sorted(set(vals)) == vals
        
        
        
        
        
        
      
        
            