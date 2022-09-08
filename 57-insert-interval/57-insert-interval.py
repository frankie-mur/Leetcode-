class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #add interval than merge
        intervals.append(newInterval)
        intervals.sort()
        
        start, end = intervals[0][0], intervals[0][1]
        res = []
        
        for i in range(1, len(intervals)):
            nxt_start, nxt_end = intervals[i][0], intervals[i][1]
            #print(end, nxt_start)
            if end >= nxt_start:
                end = max(end, nxt_end)
            else:
                res.append([start,end])
                start = nxt_start
                end = nxt_end
            
        res.append([start,end])
            
        return res
        