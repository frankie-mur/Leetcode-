class Solution:
    def canFinish(self, numCourses: int, preqs: List[List[int]]) -> bool:
        #top sort khans
        graph = defaultdict(list)
        indegree = {i:0 for i in range(numCourses)}
        for u, v in preqs:
            graph[v].append(u)
            indegree[u] += 1
        
        source = deque([])
        
        for k, v in indegree.items():
            if v == 0:
                source.append(k)
        
        counter = 0
        while source:
            node = source.popleft()
            counter += 1
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    source.append(nei)
        
        return counter == numCourses
        
        
            