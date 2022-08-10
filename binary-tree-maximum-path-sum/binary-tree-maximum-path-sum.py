# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -math.inf
        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0
            
            left_path_sum = max(dfs(node.left), 0)
            right_path_sum = max(dfs(node.right), 0)
            
            cur_path_sum = node.val + left_path_sum + right_path_sum
            
            max_sum = max(max_sum, cur_path_sum)
            
            return node.val + max(left_path_sum, right_path_sum)
        
        dfs(root)
        return max_sum
            
            