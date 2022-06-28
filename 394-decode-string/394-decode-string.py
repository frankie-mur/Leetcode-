class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ""
        num = ''
        i = 0
        for ch in s:
            if ch.isdigit():
                num += ch
            elif ch == "[":
                stack.append(int(num))
                stack.append(res)
                res = ''
                num = ''
            elif ch == "]":
                print(stack)
                res = stack.pop() + stack.pop() * res
            
            else:
                res += ch
            
        return res
                
        
            