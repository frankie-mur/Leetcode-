class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = collections.Counter(nums)
        
        for val in freq.values():
            if val >= 2:
                return True
        
        return False