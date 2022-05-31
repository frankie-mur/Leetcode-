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
        #ponter to move through LL and check if next is val
        cur = dum
        while cur.next:
            #if the cur.next is val then "delete it"
            if cur.next.val == val:
                cur.next = cur.next.next
            #this needs to be an else due to concurrent vals ex) 1->1->2->1->1
            else:
                cur = cur.next
        
        #return the dummys next which is the real head
        return dum.next
                