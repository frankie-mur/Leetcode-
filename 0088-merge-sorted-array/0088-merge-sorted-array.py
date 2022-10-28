class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        #two pointer starting from back
        
        p1, p2 = m - 1, n - 1
        cur = (m + n) - 1
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[cur] = nums1[p1]
                p1 -= 1
            else:
                nums1[cur] = nums2[p2]
                p2 -= 1
              
            cur -= 1
            
        
        