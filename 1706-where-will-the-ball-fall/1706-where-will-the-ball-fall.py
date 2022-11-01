class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        result = [0 for i in range(len(grid[0]))]

        for col in range(len(grid[0])):
            currentCol = col
            for row in range(len(grid)):
                nextColumn = currentCol + grid[row][currentCol]
                if (nextColumn < 0 or nextColumn > len(grid[0]) - 1) or (grid[row][currentCol] != grid[row][nextColumn]):
                    result[col] = -1
                    break
                
                result[col] = nextColumn
                currentCol = nextColumn
            
        
        return result;
    