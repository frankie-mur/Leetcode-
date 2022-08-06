# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #from root every value to its left should be less thatn it, and right should be greater
 
        def dfs(root):
            if not root:
                return True
            
            if dfs(root.left) == False:
                return False
            
            if root.val <= self.prev:
                return False
    
            self.prev = root.val
            
            return dfs(root.right)
            
        
        self.prev = -math.inf
        return dfs(root)
        
        
        
        
        
        
        
            