# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #for each path keep track of the current max, if the val where at is greater than or equal to current max then it is a good node
        good = 0
        def dfs(node, max_so_far):
            nonlocal good
            if not node:
                return
            
            if max_so_far <= node.val:
                good += 1
            
            dfs(node.left, max(node.val, max_so_far))
            dfs(node.right, max(node.val, max_so_far))
        
        dfs(root, -math.inf)
        return good