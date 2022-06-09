'''
U-Implement a queue using two stacks, supports all functions of a queue (FIFO)
M-simulation?, stacks
P-How can we do this...using two stacks we can use stack2 as a temp bucket to add all our values as s1 pop store our new value than push all from s2 back into s1.
I- python
R- Seems good, deque more efficent than using list?
E- All methods O(1) excpet push which is O(n) time
space: O(n) stacks depend on input
'''
class MyQueue:

    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()

    def push(self, x: int) -> None:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        while self.stack2:
            self.stack1.append(self.stack2.pop())
            
    def pop(self) -> int:
        return self.stack1.pop()
        
    def peek(self) -> int:
        return self.stack1[-1]
        

    def empty(self) -> bool:
        return len(self.stack1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()