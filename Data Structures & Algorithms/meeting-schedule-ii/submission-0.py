"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals = sorted(intervals, key=lambda inter:inter.start)
        endTime = []

        for inter in intervals:
            if endTime and endTime[0] <= inter.start:
                heapq.heappop(endTime)
            heapq.heappush(endTime,inter.end)


        return len(endTime)