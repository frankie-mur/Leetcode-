# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #reverse second half and two pointer through both
        def rev(node):
            prev = None
            while node:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
            
            return prev
        
        
        def get_mid(head):
            slow, fast = head, head
            
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            
            return slow
        
        
        mid = rev(get_mid(head))
        
        while head and mid:
            
            if head.val != mid.val:
                return False
            head = head.next
            mid = mid.next
        
        return True
        