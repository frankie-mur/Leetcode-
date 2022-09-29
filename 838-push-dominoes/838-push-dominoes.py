class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        #bfs
        q = deque()
        dominoes = list(dominoes)
        for i, dom in enumerate(dominoes):
            if dom == ".":
                continue
            
            q.append((dom, i))
        
        
        while q:
            dom, i = q.popleft()
            
            if dom == "L":
                
                if i - 1 >= 0 and dominoes[i-1] == ".":
                    dominoes[i - 1] = "L"
                    q.append(("L", i - 1))
                
            elif dom == "R":

                if i + 1 < len(dominoes) and dominoes[i + 1] == ".":
                    if i + 2 < len(dominoes) and dominoes[i + 2] == "L":
                        q.popleft()
                    
                    else:
                        dominoes[i + 1] = "R"
                        q.append(("R", i + 1))
        
        return "".join(dominoes)
            