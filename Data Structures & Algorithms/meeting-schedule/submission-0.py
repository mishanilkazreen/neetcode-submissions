"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        prev = None
        intervals = sorted(intervals, key=lambda x: x.start)
        for interval in intervals:
            if prev and prev.end > interval.start: 
                    return False
            prev = interval
        return True