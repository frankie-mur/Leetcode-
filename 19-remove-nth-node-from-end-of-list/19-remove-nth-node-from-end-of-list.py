# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #dummy node
        #fast slow to get to one before nth end
        #next = next.next
        dummy = ListNode(0)
        dummy.next = head
        
        slow, fast = dummy, head
        
        while fast and fast.next:
            fast = fast.next
            n -= 1
            if n <= 0:
                slow = slow.next
            
        slow.next = slow.next.next
        
        return dummy.next
        