class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = max(nums)
        for num in nums:
            if num != largest:
                if num * 2 > largest:
                    print(num)
                    return -1
        return nums.index(largest)