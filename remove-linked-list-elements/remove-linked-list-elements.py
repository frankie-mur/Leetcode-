# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        #dum node to remove at head
        dum = ListNode()
        dum.next = head
        #if the value is at the begining, just move the head
        while head and head.val == val:
            head = head.next
            dum.next = head
        #ponter to move through LL and check if next is val
        cur = dum
        while cur and cur.next:
            while cur.next and cur.next.val == val:
                cur.next = cur.next.next
            cur = cur.next
        
        return dum.next
                