# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        U- given a linked list return its inverse
        M- iterative 
        P- Keep track of the prev node in the LL and set the next node to its prev, do this while there is a next
        I-python
        R- this solution always works, I need to learn how to do recursively..is there an advantage?
        E- Time: O(n) for iterating through the LL
           Space: O(1) no extra space used
        
        '''
        
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        
        return prev