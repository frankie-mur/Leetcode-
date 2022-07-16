# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        """
       U: Given a binary tree return the lexigraphically smallest string that starts from leaf and ends at the root
       M: DFS,backtrack
       P: hmm what if we get all possible strings in an array and sort non-decreasing the array and return the first element? This will work whats the TC? nlogn
       Lets try it.
        """
        
        strings = []
        
        def dfs(root, path, strings):
            if not root:
                return
            
            path += chr(ord('a') + root.val)
            
            if not root.left and not root.right:
                strings.append(path[::-1])
            
           
            
            dfs(root.left, path, strings)
            dfs(root.right, path, strings)
        
        dfs(root, "", strings)
        
        
        return sorted(strings)[0]
            
            
        