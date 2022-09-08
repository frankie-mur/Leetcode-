class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort()
        
        n = len(intervals)
        res = []
        start,end = intervals[0][0], intervals[0][1]
        
        for i in range(n):
            nxt_start, nxt_end = intervals[i]
            if end >= nxt_start:
                end = max(end, nxt_end)
            else:
                res.append([start,end])
                start = nxt_start
                end = nxt_end
        
        res.append([start, end])
        
        return res