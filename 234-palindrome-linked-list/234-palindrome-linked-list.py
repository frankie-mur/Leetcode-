# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #flip second half and two pointer compare
        def reverse(head):
            prev = None
            while head:
                temp = head.next
                head.next = prev
                #this needs to be before head = temp 
                prev = head
                head = temp
                
            
            return prev
        
        fast,slow = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        
        second_head = reverse(slow)
        while head and second_head:
            if head.val != second_head.val:
                return False
            head = head.next
            second_head = second_head.next
        
        return True
                