class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        '''
        AACCGGTT -> AAACGGTA
          A    A   
          
        ["AACCGGTA","AACCGCTA","AAACGGTA"]
        bank set with byte array to tuple
        
        '''
        
        bank = set(bank)
        if end not in bank:
            return -1
        
        #current gene and the level in the graph
        q = deque()
        q.append((start, 0))
        visited = set()
        visited.add(start)
        
        while q:
            gene, level = q.popleft()
            
            if gene == end:
                return level
            
            for i in range(len(gene)):
                for ch in 'ACGT':
                    next_gene = gene[:i] + ch + gene[i+1:]
                    if next_gene in bank and next_gene not in visited:
                        visited.add(next_gene)
                        q.append((next_gene, level + 1))
        
        return -1