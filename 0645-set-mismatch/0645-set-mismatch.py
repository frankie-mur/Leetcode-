class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        dup, mis = 0, 0
        for i in range(1,len(nums) + 1):
            if i in freq:
                if freq[i] == 2:
                    dup = i
            else:
                mis = i
        
        return [dup, mis]
            
            
        
        