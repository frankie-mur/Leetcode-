# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        inorder = []
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            inorder.append(node)
            dfs(node.right)
    
        dfs(root)    
        found = 0
        for idx, num in enumerate(inorder):
            if num.val == p.val:
                found = idx
        
        if found + 1 < len(inorder):
            return inorder[found+1]
        
        return None
            
        
        