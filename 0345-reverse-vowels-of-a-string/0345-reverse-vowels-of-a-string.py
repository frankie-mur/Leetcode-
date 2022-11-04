class Solution:
    def reverseVowels(self, s: str) -> str:
        s = [ch for ch in s]
        #stack = []
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] in vowels and s[r] in vowels:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif s[l] in vowels and s[r] not in vowels:
                r -= 1
            elif s[l] not in vowels and s[r] in vowels:
                l += 1
            else:
                l += 1
                r -= 1
        
        return "".join(s)
                