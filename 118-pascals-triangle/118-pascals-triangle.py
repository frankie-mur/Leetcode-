class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascals = [[0] * i for i in range(1,numRows + 1)]
        
        
        for r in range(len(pascals)):
            for c in range(len(pascals[r])):
                #if we are at the first index of last index
                if c == 0 or c == len(pascals[r]) - 1:
                    pascals[r][c] = 1
                #we are somewhee in between
                else:    
                    pascals[r][c] = pascals[r-1][c-1] + pascals[r-1][c]
            
        
        return pascals
                    
            