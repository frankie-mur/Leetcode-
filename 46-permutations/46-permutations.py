class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        visited = set()
        res = []
        def rec(perm = []):
            if len(perm) == N:
                res.append(perm[:])
                return
            
            for num in nums:
                if num not in visited:
                    visited.add(num)
                    perm.append(num)
                    rec(perm)
                    visited.remove(num)
                    perm.remove(num)
            
        rec()
        return res
            