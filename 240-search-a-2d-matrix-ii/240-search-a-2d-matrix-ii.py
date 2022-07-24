class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])
        def bns(row):
            l, r = 0, C - 1
            
            while l <= r:
                mid = l + (r-l) // 2
                current = matrix[row][mid]
                if target == current:
                    return True
                elif target > current:
                    l = mid + 1
                else:
                    r = mid - 1
            
            return False
        
        for r in range(R):
            if bns(r):
                return True
        
        return False
                    
            
            