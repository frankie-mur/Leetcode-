class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        start,end = 0, len(graph) - 1
        adj_list = defaultdict(list)
        res = []
        for i in range(len(graph)):
            adj_list[i].extend(graph[i])
            
        def dfs(adj_list,res,cur_path, node ,end, visited):
            cur_path.append(node)
            if node == end:
                res.append(cur_path.copy())
                return
            
    
            for neig in adj_list[node]:
                dfs(adj_list,res, cur_path, neig, end, visited)
                cur_path.pop()
        
        dfs(adj_list,res, [], start, end, set())
        return res
                    
        