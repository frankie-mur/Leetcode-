class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        cur = ""
        
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            if ch == " ":
                res.append(cur)
                cur = ""
            else:
                cur += s[i]
        
        res.append(cur)
        res.reverse()
        
        return " ".join(res)