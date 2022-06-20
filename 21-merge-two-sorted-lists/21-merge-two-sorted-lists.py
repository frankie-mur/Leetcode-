# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        U-Given two linked lists merge them in sorted order
        M- two pointer
        P- have a pointer at each head and create a new list adding the smallest values from both, increment as taken
        I- python
        R- passes test casses, thinking about a way to use constant space...hmmm
        E- Space: O(n) -> for the result linked list
           Time: O(n) -> for passes through both l1 and l2
        
        '''
        dum = ListNode(0)
        res = dum
        while l1 and l2:
            if l1.val > l2.val:
                res.next = ListNode(l2.val)
                l2 = l2.next
            else:
                res.next = ListNode(l1.val)
                l1 = l1.next
            
            res = res.next
        
        if l1:
            res.next = l1
        if l2:
            res.next = l2
        
        return dum.next
            
        
        