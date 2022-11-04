# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #merge sort
        def halve(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
        
            return slow
        
        def merge(head1, head2):
            dummy = ListNode(-1)
            new_list = dummy
            
            while head1 and head2:
                if head1.val < head2.val:
                    new_list.next = head1
                    head1 = head1.next
                else:
                    new_list.next = head2
                    head2 = head2.next
                
                new_list = new_list.next
            
            if head1:
                new_list.next = head1
            
            if head2:
                new_list.next = head2
            
            return dummy.next
        
        
        if not head or not head.next:
            return head
        
        left = head
        right = halve(head)
        
        
        temp = right.next
        right.next = None
        right = temp
        
        left = self.sortList(left)
        right = self.sortList(right)
        
    
        return merge(left, right)
        
        
            