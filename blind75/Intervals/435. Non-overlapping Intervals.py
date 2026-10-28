# https://leetcode.com/problems/non-overlapping-intervals/

'''
这道题是说给一些有overlapping的interval
最少删除几个intervals可以让剩下的interval non-overlapping

采用贪心法
1.对intervals排序
2.从左到右遍历Intervals, 如果有overlap，就删除end time晚的interval
原理是结束时间晚的区间更有可能和后面的区间overlap
'''

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:x[0])

        remove = 0
        # start = intervals[0][0] # no need start
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < end: # have overlap
                remove += 1
                end = min(intervals[i][1], end) # keep interval with early end
            else: # no overlap, move end to next interval end
                end = intervals[i][1]

        return remove

if __name__ == '__main__':
    s = Solution()
    print(s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
    print(s.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
    print(s.eraseOverlapIntervals([[1,2],[2,3]]))
    print(s.eraseOverlapIntervals([[1,2]]))
