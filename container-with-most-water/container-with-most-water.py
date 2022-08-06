class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxc = 0
        while l < r:
            dist = r - l
            h = min(heights[l], heights[r])
            maxc = max(maxc, dist * h)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxc