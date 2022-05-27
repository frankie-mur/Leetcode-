# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        '''
        -reorder the list -> inplace?
        -cannot modify values
        hmmm....we can reverse the second half, and have pointer at start and second half then set next pointers and move
        ex)
        
        1->2->3->4->null
        1) rev second half
        1->2->4->3->null
        2)pointers and begining and second half
        1->2->4->3->null
        p1   p2 
        3)set p1.next to p2 then move both pointers
         res = 1->4->2->3      
        '''
        
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #reverse second half
        half = slow.next
        prev = slow.next = None
        while half:
            temp = half.next
            half.next = prev
            prev = half
            half = temp
        
        #now prev is at the half reversed
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first,second = tmp1, tmp2
            
     