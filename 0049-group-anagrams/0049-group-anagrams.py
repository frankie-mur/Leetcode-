class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #sort each word and group if the sorted words are the same
        ana = defaultdict(list)
        res = []
        
        for word in strs:
            ana[''.join(sorted(word))].append(word)
        
        
        return [lis for lis in ana.values()]
        
        