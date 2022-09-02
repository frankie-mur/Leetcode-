# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        prefix = defaultdict(int)
        
        def preorder_dfs(node, cur_sum):
            if not node:
                return
            
            cur_sum += node.val
            if cur_sum == targetSum:
                self.count += 1
                
            diff = cur_sum - targetSum
            self.count += prefix[diff]
            prefix[cur_sum] += 1
            
            preorder_dfs(node.left, cur_sum)
            preorder_dfs(node.right, cur_sum)
            
            prefix[cur_sum] -= 1
        
        
        preorder_dfs(root, 0)
        return self.count
            
            
            
        