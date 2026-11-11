class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals = sorted(intervals, key=lambda interval:interval[1])

        ret = 0
        last = intervals[0][0] - 1
        for interval in intervals:
            if last > interval[0]:
                ret += 1
            else :
                last = interval[1]

        return ret