class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort()
        
        res = []
        n = len(intervals)
        start, end = intervals[0][0], intervals[0][1]
        for first, second in intervals:
            if end >= first:
                end = max(end, second)
            else:
                res.append([start,end])
                start = first
                end = second
        
        res.append([start,end])
        
        return res