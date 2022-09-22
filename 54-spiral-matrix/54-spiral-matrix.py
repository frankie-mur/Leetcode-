class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        
        
        while left <= right and top <= bottom:
            #top left to right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            
            #top right to bottom right
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            
            #bottom right to bottom left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1
            
            #bottom left to top left
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res
            