# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        #go thorugh each path keeping a dictionary of the digits in it, if the length is odd it needs all evens and one odd, if even it needs all evens
        
        count = defaultdict(int)
        res = 0
        def is_psuedo_pali(count, length):
            if length % 2 == 0:
                #here it is even therefore we need all evens ch counts
                for val in count.values():
                    if val % 2 != 0:
                        return False
                return True
            else:
                odd = False
                #odd we need all evens and one odd
                for val in count.values():
                    if val % 2 != 0:
                        if odd:
                            return False
                        else:
                            odd = True
                return True
            
        def dfs(node, length):
            if not node:
                return 
            
            nonlocal count
            length += 1
            count[node.val] += 1
            if not node.left and not node.right and is_psuedo_pali(count, length):
                nonlocal res
                res += 1
                
            dfs(node.left, length + 1)
            dfs(node.right, length + 1)
            count[node.val] -= 1
            
        
        dfs(root, 0)
        return res