class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        '''
        U- Given a matrix return the transpose of said matrix. 
        What is transpose? flipped over diangonal switching row's and column indices
        ex) [[1,2,3],[4,5,6]] -> [[1,4],[2,5],[3,6]] 
        M- Simulation
        P- Create a res array of M*N, for loop to append res[r][c] -> matrix[c][r] where r is row a c is column
        I- coded below
        R- seems okay
        E- Space: O(n) for length of matrix
           Time: O(n^2) for nested for loop through matrix 
        
        '''
        M = len(matrix)
        N = len(matrix[0])
        res = [[0] * M for _ in range(N)]
        for r in range(N):
            for c in range(M):
                res[r][c] = matrix[c][r]
        
        return res
        
        
        
        