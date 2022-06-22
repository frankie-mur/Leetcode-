# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        U-If a list contains a cycle return where that cycle starts
        M-Fast and slow pointer
        P-First find if there is a cycle, if there is then start a new pointer from the beginning and increment till the previous pointer and the new one collide, this is the start. Can be proven with math 
        I- Python
        R- Works for all test cases
        E- Time: O(n)
            Space: O(1)
        '''
        slow,fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                #CYCLE!
                start = head
                while start != slow:
                    start,slow = start.next,slow.next
                
                return start
        
        return 
        
        