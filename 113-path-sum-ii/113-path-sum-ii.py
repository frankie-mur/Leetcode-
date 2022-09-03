# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        res = []
        
        def dfs(node: Optional[TreeNode], cur_path: list, curr_sum: int) -> None:
            if not node:
                return
            
            curr_sum += node.val
            
            if not node.left and not node.right and curr_sum == targetSum:
                res.append(cur_path + [node.val])
            
            
            dfs(node.left, cur_path + [node.val], curr_sum)
            dfs(node.right, cur_path + [node.val], curr_sum)
        
        
        dfs(root, [], 0)
        
        return res
            
            
            