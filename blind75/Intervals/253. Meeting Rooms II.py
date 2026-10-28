# https://leetcode.com/problems/meeting-rooms-ii/
# https://neetcode.io/problems/meeting-schedule-ii/question?list=blind75

'''
这个题特别好！将时间区间转换为event的概念
'''

from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def toInterval(l):
        res = []
        for e in l:
            res.append(Interval(e[0], e[1]))
        return res


'''
这个题思路特别好
不要被之前252题目迷惑，这两个有本质区别
252是有一个人，相当于一个room, 不能有任何inteval overlap
253是给定interval, 计算同时最多需要几个room

思路是把start, end转化成event，event代表某一时刻room需要+1还是-1
start event 需要的room + 1
end event 需要的room - 1

对event排序，先按时间排序，如果时间一样就把end event排在start event之前，
意味着先释放room,
比如排序后[(1, 1), (2, 1), (3, 1), (4, 1), (5, -1), (5, 1), (6, -1), (7, -1), (8, -1), (9, -1)]
其中有(5, -1), (5, 1)
在时刻5就是先room-1，再room+1

之后从头到尾遍历event, 同时累加event的room变化，得到同时需要的最大rooms数量
'''
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        event = [] # 保存在时刻start/end, room+1 or room-1
        for i in intervals:
            event.append((i.start, 1))
            event.append((i.end, -1))

        event.sort(key=lambda x: (x[0], x[1]))
        # print(event)

        room = 0
        maxRoom = 0
        for e in event:
            room += e[1]
            maxRoom = max(maxRoom, room)

        return maxRoom


'''
思路
找出连续conflict intervals最大个数, 我理解错了，会议可以结束就释放会议室了
这个思路不通
'''
class SolutionWrong:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0

        maxRoom = 1
        room = 1
        intervals.sort(key=lambda x:x.start)
        for i in range(1, len(intervals)):
            intv1 = intervals[i-1]
            intv2 = intervals[i]
            
            if intv2.start < intv1.end:
                room += 1
            else:
                maxRoom = max(maxRoom, room)
                room = 1
        print(maxRoom, room)
        return max(maxRoom, room)
    

if __name__ == '__main__':
    s = Solution()
    print(s.minMeetingRooms(Interval.toInterval([(0,40),(5,10),(15,20)])))
    print(s.minMeetingRooms(Interval.toInterval([(1,5),(2,6),(3,7),(4,8),(5,9)])))