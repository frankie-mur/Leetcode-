class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq1 = collections.Counter(arr1)
        res = []
        seen = set(arr2)
        rem = []
        for num in arr1:
            if num not in seen:
                rem.append(num)
        print(rem)
        
        seen = set(arr2)
                
        for num in arr2:
            res.extend([num] * freq1[num])
        
        res.extend(sorted(rem))
        
        return res
            
        