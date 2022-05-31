# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #fast slow pointer
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            #cycle, now find where it starts
            #this is done by starting a new pointer at head 
            # and moving until slow(or fast) pointers collide with new res
            if slow == fast:
                res = head
                while slow:
                    if res == slow:
                        return res
                    res = res.next
                    slow = slow.next
                    
                
        #no cycle
        return None
        