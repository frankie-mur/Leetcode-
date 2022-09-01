# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddHead, evenHead = ListNode(-1), ListNode(-1)
        odd, even = oddHead, evenHead
        
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
        
        odd.next = evenHead.next
        even.next = None
        
        return oddHead.next