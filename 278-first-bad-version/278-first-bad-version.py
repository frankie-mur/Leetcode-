# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        #find the first version of true after a false
        l, r = 1, n
        
        while l <= r:
            mid = l + (r - l) // 2
            
            is_bad = isBadVersion(mid)
            
            if is_bad == True:
                r = mid - 1 
            
            else:
                l = mid + 1
                
        return l
        
        
        '''
        [1,2,3,4,5,6,7,8,9,10]
         l                  r
        
        '''