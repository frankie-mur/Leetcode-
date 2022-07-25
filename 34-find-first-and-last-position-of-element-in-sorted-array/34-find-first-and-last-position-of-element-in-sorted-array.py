class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bns(nums, target, searched):
            l, r = 0, len(nums) - 1
            ans = -1
            while l <= r:
                mid = l + (r - l) // 2
                if target == nums[mid]:
                    ans = mid
                    if not searched:
                        r = mid - 1
                    else:
                        l = mid + 1
                elif target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            
            return ans
        
        ans = [-1,-1]
        ans[0] = bns(nums,target,False)
        ans[1] = bns(nums,target,True)
        
        return ans
        
        
        
        
        
        
        
        
            
            
                
                    