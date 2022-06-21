# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(rootL, rootR):
            if not rootL and not rootR:
                return True
            if not rootL or not rootR:
                return False
            
            return rootL.val == rootR.val and dfs(rootL.left, rootR.right) and dfs(rootL.right, rootR.left)
        l = root.left
        r = root.right
        ans = dfs(l,r)
        return ans
            
            
        