class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort()
        
        res = []
        start, end = intervals[0][0], intervals[0][1]
        for idx in range(1,len(intervals)):
            next_start, next_end  = intervals[idx][0], intervals[idx][1]
            if end >= next_start:
                end = max(end, next_end)
            else:
                res.append([start,end])
                start, end = next_start, next_end
                
        res.append([start,end])        
                
        return res
            