# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        two pointer and dummynode
        traverse the LL with cur and prev while cur and cur has a next
        temp variables to hold nodes whos links will be broken
        reverse and update pointers
        '''
        dum = ListNode(0)
        dum.next = head
        prev, cur = dum, head
        while cur and cur.next:
            #save tmp variables
            nxtPair = cur.next.next
            second = cur.next
            #reverse pair
            second.next = cur
            cur.next = nxtPair
            prev.next = second
            #update ptrs
            prev = cur
            cur = nxtPair
        
        return dum.next