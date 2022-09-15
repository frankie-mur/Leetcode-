class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()
        def dfs(cur_perm):
            if len(cur_perm) == len(nums):
                res.append(cur_perm.copy())
                return
            
            for num in nums:
                if num not in visited:
                    cur_perm.append(num)
                    visited.add(num)
                    dfs(cur_perm)
                    cur_perm.remove(num)
                    visited.remove(num)
        
        dfs([])
        return res
                    
                
                