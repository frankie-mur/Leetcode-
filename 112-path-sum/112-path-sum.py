# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(root, sum_):
            if not root:
                return False
            
            if not root.left and not root.right and (sum_ - root.val) == 0:
                return True
            
            return dfs(root.left, sum_ - root.val) or dfs(root.right, sum_ - root.val)
        
        
        return dfs(root, targetSum)