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
            
            if not node.left and not node.right and cur_sum == targetSum:
                cur_path += [node.val]
                res.append(cur_path)
                #return
                
            dfs(node.left, cur_path + [node.val], cur_sum)
            dfs(node.right, cur_path + [node.val], cur_sum)
            
        
        res = []
        dfs(root, [], 0)
        return res
                
            
            