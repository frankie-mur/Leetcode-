# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #get the two numbers as a string and reverse and sum
        num1, num2 = '',''
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        
        total = int(num1[::-1]) + int(num2[::-1])
        
        total = str(total)
        total = total[::-1]
        
        dum = ListNode(0)
        res = dum
        
        for ch in total:
            dum.next = ListNode(int(ch))
            dum = dum.next
        
        return res.next
        