class Solution:
    def findOrder(self, numCourses: int, preqs: List[List[int]]) -> List[int]:
        #implement khans topological sort
        graph = defaultdict(list)
        indegree = {i:0 for i in range(numCourses)}
        
        for u, v in preqs:
            graph[v].append(u)
            indegree[u] += 1

            
        source = deque([])
        
        for key,val in indegree.items():
            if val == 0:
                source.append(key)
        
        index = 0
        res = [0 for _ in range(numCourses)]
        while source:
            course = source.popleft()
            res[index] = course
            index += 1
            
            for nei in graph[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    source.append(nei)
        
        
        return res if index == numCourses else []
             
        
            