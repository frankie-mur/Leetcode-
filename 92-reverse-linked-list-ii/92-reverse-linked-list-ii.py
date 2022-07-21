# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #need to keep track of one before left and one after right
        def reverse(head):
            prev = None
            while head:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            
            return prev
            
        
        if left == right:
            return head
        
        dum = ListNode(-1)
        dum.next = head
        
        pos_r, pos_l = 1, 1
        r_head, l_head = None,None
        prev_l_head = None
        l_tail = None
        prev = None
        while head:
            if pos_l == left:
                l_head = head
                prev_l_head = prev
            if pos_r == right:
                r_head = head
                r_tail = r_head.next
                break
            prev = head
            head = head.next
            pos_r += 1
            pos_l += 1

        r_head.next = None
        reverse(l_head)
        
        if l_head:
        
            l_head.next = r_tail
        if prev_l_head:
            prev_l_head.next = r_head
        else:
            return r_head
        
  
            
        
            
        
        return dum.next
            
        
        
        
        
            