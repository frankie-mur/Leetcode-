# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        
        
        '''
        
        dummy_odd, dummy_even = ListNode(-1), ListNode(-1)
        odd, even = dummy_odd, dummy_even
        
        is_odd = True
        
        while head:
            if is_odd:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
                
            head = head.next
            is_odd = not is_odd
        
        odd.next = dummy_even.next
        even.next = None
        
        return dummy_odd.next