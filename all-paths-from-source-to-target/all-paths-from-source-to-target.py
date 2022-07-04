class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        start,end = 0, len(graph) - 1
        res = []
        def dfs(vertex, cur_path,res):
            cur_path.append(vertex)
            
            if vertex == end:
                res.append(cur_path.copy())
            #dont need to check visited bc directed graph
            for neig in graph[vertex]:
                dfs(neig, cur_path, res)
                #pop here to remove backtrack cur_path
                cur_path.pop()
        
        dfs(start,[],res)
        
        return res
                
            
        