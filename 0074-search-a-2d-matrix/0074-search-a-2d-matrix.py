class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #binary search row 
        R, C = len(matrix), len(matrix[0])
        t, b = 0, R - 1
        row = 0
        while t <= b:
                row = (t + b) // 2

                if target > matrix[row][C-1]:
                    t += 1
                elif target < matrix[row][0]:
                    b -= 1
                else:
                    break
            
        if t > b:
            return False
            
        def bns(row, l, r):
            while l <= r:
                mid = l + r // 2
                
                if matrix[row][mid] == target:
                    return True
                
                elif target > matrix[row][mid]:
                    l += 1
                
                else:
                    r -= 1
            
            return False
        
    
        return bns(row, 0, C-1)
     
        
            
'''
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #first binart seach for the row
        R, C = len(matrix), len(matrix[0])
        top, bottom = 0, R - 1
        row = 0
        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][C - 1]:
                top += 1
            elif target < matrix[row][0]:
                bottom -= 1
            else:
                break
            
        if top > bottom:
            return False
        print("here")
        def bns(array, target):
            l, r = 0, len(array) - 1

            while l <= r:
                mid = (l + r) // 2

                if target == array[mid]:
                    return True
                elif target > array[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            
            return False
        
        return bns(matrix[row], target)

'''