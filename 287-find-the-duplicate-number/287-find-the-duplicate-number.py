class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #fast n slow pointers
        #linked list problem with floyd cycle detection
        slow, fast = 0 , 0
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            #intersection of cycles
            if slow == fast:
                break
        
        head = 0
        while True:
            slow = nums[slow]
            head = nums[head]
            #begining of cycle
            if slow == head:
                return head
            
        return None
    
        
    
    
