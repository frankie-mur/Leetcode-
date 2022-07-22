# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        '''
        Convert to grap, do a bfs keeping track of distance from target
        '''
        def to_graph(node, parent, graph):
            if not node:
                return
            if parent:
                graph[node].append(parent)
            
            if node.left:
                graph[node].append(node.left)
                to_graph(node.left, node, graph)
            
            if node.right:
                graph[node].append(node.right)
                to_graph(node.right, node, graph)
        
        graph = collections.defaultdict(list)
        to_graph(root, None, graph)
        
        q = deque([target])
        visited = set()
        res = []
        distance = 0
        while q:
            size = len(q)
            for _ in range(size):
                vertex = q.popleft()
                visited.add(vertex)
                if distance == k:
                    res.append(vertex.val)
                
                for nei in graph[vertex]:
                    if nei not in visited:
                        q.append(nei)
            
            distance += 1
                    
        return res
                       
        
                
                
                
        
            
                
                
        
        
        
        
        
        
                
            
            