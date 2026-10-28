# https://leetcode.com/problems/meeting-rooms/
# https://neetcode.io/problems/meeting-schedule/question?list=blind75

'''
题目是说给定一些时间区间，判断是否有Overlap
区间的顺序不固定

是一个人指定日程，不能有任何overlap
'''


from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

'''
思路
按照start time排序
之后比较相邻俩个是否有overlap
'''
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)

        for i in range(1, len(intervals)):
            intv1 = intervals[i-1]
            intv2 = intervals[i]
            if intv2.start < intv1.end:
                return False
        return True

# if __name__ == '__main__':
#     s = Solution()
#     print(s.canAttendMeetings())