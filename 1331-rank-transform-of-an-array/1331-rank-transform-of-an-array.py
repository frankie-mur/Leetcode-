class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        dic = {}
        
        counter = 0
        for num in sorted(arr):
            if num not in dic:
                counter += 1
                dic[num] = counter
            else:
                dic[num] = counter
        
        res = []
        
        for num in arr:
            res.append(dic[num])
        
        return res
        
            