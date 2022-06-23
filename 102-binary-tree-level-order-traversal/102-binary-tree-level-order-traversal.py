# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #classic bfs have an array to append values too 
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            cur_lvl = []
            for _ in range(len(q)):
                cur_node = q.popleft()
                cur_lvl.append(cur_node.val)
                
                if cur_node.left:
                    q.append(cur_node.left)
                
                if cur_node.right:
                    q.append(cur_node.right)
                
            res.append(cur_lvl)
        
        return res