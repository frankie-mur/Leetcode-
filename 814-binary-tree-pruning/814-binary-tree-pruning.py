# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #brute force, find nodes with zero and check if all subtrees are zero
        
        def subtree_zero(node):
            if not node:
                return True
            
            if node.val == 1:
                return False
            
            return node.val == 0 and subtree_zero(node.left) and subtree_zero(node.right)
        
        
        def dfs(root):
            if not root:
                return
            
            #print(root.left, subtree_zero(root.left))
            if root.left and root.left.val == 0 and subtree_zero(root.left):
                root.left = None
            
            if root.right and root.right.val == 0 and subtree_zero(root.right):
                root.right = None
            
            dfs(root.left)
            dfs(root.right)
        
        dummy = TreeNode()
        dummy.right = root
        dfs(dummy)
        return dummy.right