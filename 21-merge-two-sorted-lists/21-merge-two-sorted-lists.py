# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #create a dummy node to have a pointer to the head
        dum = ListNode(0)
        res = dum
    
        
        while l1 and l2:
            #append to res using two pointer in non-decreasing order
            if l1.val < l2.val:
                res.next = l1
                l1 = l1.next
            else:
                res.next = l2
                l2 = l2.next
            
            res = res.next
        #if there are left over values
        while l1:
            res.next = l1
            l1 = l1.next
            res = res.next
        while l2:
            res.next = l2
            l2 = l2.next
            res = res.next
        
        return dum.next
            
            
            