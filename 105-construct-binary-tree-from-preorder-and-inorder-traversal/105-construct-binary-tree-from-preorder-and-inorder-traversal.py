# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        lookup = {}
        for i, num in enumerate(inorder):
            lookup[num] = i
        
        current = 0
        def pre_order_trav(left, right):
            if left > right:
                return None
            nonlocal current
            
            root = preorder[current]
            current += 1
            
            mid = lookup[root]
            
            node = TreeNode(root)
            
            node.left = pre_order_trav(left, mid - 1)
            node.right = pre_order_trav(mid + 1, right)
            
            return node
        
        return pre_order_trav(0,len(inorder)-1)
            