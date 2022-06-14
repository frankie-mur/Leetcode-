class Solution:
    def frequencySort(self, s: str) -> str:
        '''
        U- Given a string return the string sorted in decresing order based on frequency of the ch, if freq is the same the order does not matter.
        s = 'tree' -> 'eert' or ''eetr
        freq = 't':1, 'r':1. 'e': 2
        lis_freq = [(e,2), (t,1), (r,1)]
        res = 'eetr'
        M- hashmap to store freq of chars.
        
        P- Sort the freq map into a non-increasing list than loop through the list and append (ch * freq) 
        
        I-python
        
        R-
        
        E-
        
        
        '''
        freq = {}
        for ch in s:
            freq[ch] = freq.setdefault(ch, 0) + 1
        
        freq_lis = []
        for key,val in freq.items():
            freq_lis.append((val,key))
        
        freq_lis.sort(reverse=True)
        
        res = ''
        for f,ch in freq_lis:
            res += ch * f
        
        return res