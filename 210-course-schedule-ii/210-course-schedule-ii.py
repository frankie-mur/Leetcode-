class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        
        indegree = {i:0 for i in range(numCourses)}
        
        graph = defaultdict(list)
        source = deque([])
        
        for v, u in prerequisites:
            graph[u].append(v)
            indegree[v] += 1
        
        
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
            