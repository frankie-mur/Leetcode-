# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        U - Given a linked list we want to remove the n'th node from the end of the list and return the lists head
        M - Fast and slow pointer? 
        P - In order to get to the N'th from end in one pass we can use a two pointer technique, we start the fast pointer and decrement n for every next. Once n is below zero we can increment the slow pointer. When fast reaches the end then it will be one before the n'th. Then we can make the slow pointer next = next.next
        I - Python
        R - Seems to pass odd casses
        E - Time: O(N) One pass throught the list
            Space: O(1)
        
        
        '''
        
        dummy = ListNode(-1)
        dummy.next = head
        slow,fast = dummy,dummy
        
        while fast.next:
            fast = fast.next
            n -= 1
            if n < 0:
                slow = slow.next
        
        slow.next = slow.next.next
    
        
        return dummy.next
            