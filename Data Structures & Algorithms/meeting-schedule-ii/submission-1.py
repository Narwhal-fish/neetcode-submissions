"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        end = []
        intervals = sorted(intervals, key=lambda inter:inter.end)
        last = intervals[0].end

        for inter in intervals:
            if last > inter.start:
                if end and end[0] <= inter.start:
                    heapq.heappop(end)
                else :
                    heapq.heappush(end, inter.end)

        return len(end)

            

            
        