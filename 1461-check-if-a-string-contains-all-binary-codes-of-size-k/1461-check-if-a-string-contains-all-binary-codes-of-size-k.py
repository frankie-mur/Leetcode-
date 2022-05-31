class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = set()
        q = deque()
        for c in s:
            q.append(c)
            if len(q) == k: 
                seen.add(''.join(q))
                q.popleft()
        return len(seen) == 1 << k