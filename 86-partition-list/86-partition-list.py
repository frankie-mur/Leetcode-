# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        '''
        P: Get all values in the order that they come, store the sort of these values,
        Create the linked list with the sort until we reach x, now go back to the origal values,
        if we havent used yet than we add
        R: Seem good, passes some weird test casses
        E: Time: O(nlogn)
            Space: O(n)
        '''
        
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        dummy = ListNode(-1)
        new_head = dummy
        seen = set()
        current = 0
        for num in vals:
            if num < x:    
                new_head.next = ListNode(num)
                seen.add(num)
                new_head = new_head.next

        for num in vals:
            if num not in seen:
                new_head.next = ListNode(num)
                new_head = new_head.next
        
        return dummy.next
        
        
        
            
            
        
        
        