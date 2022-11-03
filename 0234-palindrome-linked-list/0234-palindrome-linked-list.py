# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #get to half and reverse, then check if both sides are equal
        
        def rev(head):
            prev = None
            
            while head:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            
            return prev
        
        
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        
        first, half = head, rev(slow)
        
        while first and half:
            if first.val != half.val:
                return False
            first = first.next
            half = half.next
        
        return True
                