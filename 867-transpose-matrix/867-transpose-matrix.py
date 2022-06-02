class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        '''
        U- Given a matrix return the transpose of said matrix. 
        What is transpose? flipped over diangonal switching row's and column indices
        ex) [[1,2,3],[4,5,6]] -> [[1,4],[2,5],[3,6]] 
        M- Simulation
        P- Create a res array of M*N, for loop need to go matrix[i][0] -> end and append to res[0][i]
        I- 
        R-
        E-
        
        '''
        M = len(matrix)
        N = len(matrix[0])
        res = [[0] * M for _ in range(N)]
        for r in range(N):
            for c in range(M):
                res[r][c] = matrix[c][r]
        
        return res
        
        
        
        