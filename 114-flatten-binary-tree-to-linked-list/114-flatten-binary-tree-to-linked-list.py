# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Input: root node of binary tree
        Output: convert binary tree to right-skewed linked list
        """
        
        # record of node of previous traversal
        previous_traversal = None
        
        def helper( node):
        
            if node:

                # DFS travesal to next level
                
                helper( node.right )
                helper( node.left )

                # flattern binary tree to right skewed linked list
                
                nonlocal previous_traversal
                node.right = previous_traversal
                node.left = None
                previous_traversal = node
                
        # ---------------------
        
        helper(root)
        