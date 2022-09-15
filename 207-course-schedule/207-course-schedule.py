class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        #top sort
        graph = defaultdict(list)
        indegree = {i:0 for i in range(numCourses)}
        for pre, class_ in pre:
            graph[pre].append(class_)
            indegree[class_] += 1
        
        source = deque()
        
        for key,val in indegree.items():
            if val == 0:
                source.append(key)
        
        classes = 0
        while source:
            course = source.pop()
            classes += 1
            for nei in graph[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    source.append(nei)
        
        return classes == numCourses
        
        
        
            