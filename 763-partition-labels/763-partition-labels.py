class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = Counter(s)
        #traverse throught the string until everthing we have seen to far has a freq of zero once this happends we leave and append the length
        taken = set()
        count = 1
        res = []
        def check_vals(taken):
            for vals in taken:
                if freq[vals] != 0:
                    return False
            return True
        
        for ch in s:
            taken.add(ch)
            freq[ch] -= 1
            if check_vals(taken):
                res.append(count)
                count = 0
            count += 1
        
        return res
            
                
                    
        