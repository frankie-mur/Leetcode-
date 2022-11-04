class Solution:
    def reverseVowels(self, s: str) -> str:
        s = [ch for ch in s]
        stack = []
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        for ch in s:
            if ch in vowels:
                stack.append(ch)
        
        for i, ch in enumerate(s):
            if ch in vowels:
                s[i] = stack.pop()
        
        return "".join(s)
                