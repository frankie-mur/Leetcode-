# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        remove nth from end, how do we get there?
        dummy head to help with edge cases
        two pointer, move n spots with first then start second at head move both until first reaches end, second will be at nth end - 1
        ex)
        0->1->2->3->4->5    n = 2
        p2    p1
        
        1->2->3->4->5
              p2    p1
              
        set p2->next to next->next
        '''
        dum = ListNode()
        dum.next = head
        slow,fast = dum,head
        while fast and fast.next:
            fast = fast.next
            n -= 1
            if n <= 0:
                slow = slow.next
        
        slow.next = slow.next.next
        
        return dum.next