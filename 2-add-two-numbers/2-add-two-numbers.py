# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #logicaly
        total = 0
        carry = 0
        dum = res = ListNode()
        
        #while theres still values in linked list or if theres a carry remaining
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry
            #you dont need to check if carry > 9 bc if less than 10 will eval to 0
            # // 10 will get the first digit in any int
            carry = total // 10
            #total only needs the ones place
            total = total % 10
            #add the value to the resulting LinkedList
            res.next = ListNode(total)
            res = res.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        
        return dum.next
                
        