class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        '''
        First thought is check left to right but cant find a distanct order?
        Unless I go bottom left to top and top to far right?
        '''
        #start bottom left and check if it has diaganol
        
            
        R, C = len(matrix), len(matrix[0])
        
        start = (R - 1, 0)
        end = (0, C - 1)
        def check_diag(r, c):
            while r + 1 < R and c + 1 < C:
                if matrix[r][c] != matrix[r + 1][c + 1]:
                    return False
                r += 1
                c += 1
            return True
        
        r, c = R - 1, 0
        
        while c <= C - 1:
            if not check_diag(r, c):
                return False
            if r > 0:
                r -= 1
            else:
                c += 1
            
        return True