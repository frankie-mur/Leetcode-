# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        odd, even = ListNode(-1), ListNode(-1)
        
        oddHead, evenHead = odd, even
        is_odd = True
        while head:
            if is_odd:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
        
            is_odd = not is_odd
            head = head.next
        
        even.next = None
        odd.next = evenHead.next
        
        return oddHead.next
        
            
        
        