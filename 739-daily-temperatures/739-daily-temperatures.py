class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        '''
        U-given temp return a list that represents such that answer[i] = the days you have to wait until a hotter day at temp[i] if none make == 0
        M-Brute force is simple, but we can improve with a monotonic stack
        P-Have res be prepended with zeros and create a stack, loop through temp keeping track of both index and temp val. If there is a stack and the prev value is less than the current temp val than we can pop and we have an answer for prev_i which is current i - prev_i (distance). If not keep appending to the stack
        I- python
        R- Passes test cases seems to work for all test casses
        E- Time: O(n) one pass of temp
           Space: O(n) monotonic stack
        '''
        stack, res = [], [0 for _ in range(len(temp))]
        
        for i,t in enumerate(temp):
            while stack and stack[-1][1] < t:
                prev_i, prev_t = stack.pop()
                res[prev_i] = i - prev_i
            
            stack.append((i,t))
        
        return res
             