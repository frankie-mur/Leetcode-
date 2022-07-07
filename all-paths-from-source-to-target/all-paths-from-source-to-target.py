class Solution:
    def allPathsSourceTarget(self, G: List[List[int]]) -> List[List[int]]:
        ans, q = [], deque([[0]])
        while q:
            path = q.popleft()
            if path[-1] == len(G)-1: ans.append(path)
            else:
                q.extend(path + [child] for child in G[path[-1]])
        return ans
                
            
        