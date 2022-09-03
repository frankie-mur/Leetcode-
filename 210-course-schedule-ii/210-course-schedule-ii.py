class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #khans top sort
        source = deque([])
        res = [0 for _ in range(numCourses)]
        
        graph = defaultdict(list)
        indegree = {i:0 for i in range(numCourses)}
        
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        for course, inde in indegree.items():
            if inde == 0:
                source.append(course)
        
        
        
        index = 0
        while source:
            size = len(source)
            for _ in range(size):
                
                course = source.popleft()
                res[index] = course
                index += 1
                
                for nei in graph[course]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        source.append(nei)
        
        return res if index == numCourses else []
    
        
        