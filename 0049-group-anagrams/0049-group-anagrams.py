class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #sort each word and group if the sorted words are the same
        ana = defaultdict(list)
        
        
        for word in strs:
            freq = [0] * 26
            
            for ch in word:
                freq[ord(ch) - ord('a')] += 1
            
            ana[tuple(freq)].append(word)
        
        return [lis for lis in ana.values()]
        
        