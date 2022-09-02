# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0
        
        def dfs(node, path_max_sum):
            if not node:
                return
            
            if node.val >= path_max_sum:
                self.good += 1
            
            dfs(node.left, max(path_max_sum, node.val))
            dfs(node.right, max(path_max_sum, node.val))
        
        
        dfs(root, root.val)
        return self.good