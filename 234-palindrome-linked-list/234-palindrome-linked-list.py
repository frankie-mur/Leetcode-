# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #flip second half then two pointer through
        
        def rev(head):
            prev = None
            while head:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            
            return prev
        
        slow, fast = head,head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        half = rev(slow)
        p = head
        
        while p and half:
            if p.val != half.val:
                return False
            p = p.next
            half = half.next
        
        return True
        
        
                
        