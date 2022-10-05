# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val=val,left=root)
        
        work_queue = collections.deque([(root)])
        level = 1
        
        while work_queue and depth - 1 != level: # here is added the condition depth-1 != level which means we stop as soon as we hit the parent row
            nr_of_node_level = len(work_queue)
            for _ in range(nr_of_node_level):
                current_node = work_queue.popleft()
                
                if current_node.left:
                    work_queue.append(current_node.left)
                if current_node.right:
                    work_queue.append(current_node.right)
            level += 1
            
        for current_node in work_queue:
            current_node.left = TreeNode(val=val,left=current_node.left)
            current_node.right = TreeNode(val=val,right=current_node.right)
        
        return root