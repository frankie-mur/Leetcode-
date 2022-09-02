# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def dfs(node, cur_path, cur_sum):
            if not node:
                return
            
            cur_sum += node.val
            cur_path.append(node.val)
            if not node.left and not node.right and cur_sum == targetSum:
                nonlocal res
                res.append(cur_path.copy())
            
            dfs(node.left, cur_path, cur_sum)
            dfs(node.right, cur_path, cur_sum)
            cur_path.pop()
        
        
        res = []
        dfs(root, [], 0)
        return res
                
            
            