class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        '''
        U-find the min path sum from top to bottom of 2d array: but it you can only move to the index your one or index+1 to the next row
        M-DP?, recursion
        P-recursive top down function that recursies down for both i and i+1
        I-python
        R-passes test casses
        E- Time: O(n*m)
           Space: O(n*m)
        '''
        for level in range(len(triangle)-2,-1,-1):
            for i in range(level+1):
                triangle[level][i] += min(triangle[level+1][i], triangle[level+1][i+1])
        return triangle[0][0]

