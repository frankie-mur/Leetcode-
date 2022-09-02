# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        avg = []
        
        q = deque([root])
        
        while q:
            size = len(q)
            cur_avg = 0
            for _ in range(size):
                cur = q.popleft()
                cur_avg += cur.val
                
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            
            avg.append(cur_avg / size)
        
        return avg