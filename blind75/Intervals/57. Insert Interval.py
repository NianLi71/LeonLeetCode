# https://leetcode.com/problems/insert-interval/


from typing import List

'''
总结
我比较思路3和2
思路3很简洁
思路2是在56题基础上改进来的，有连贯性
'''


'''
思路3
做最简单的搜索
不要考虑56题思路
因为已经排序过了，直接扫一遍做merge

对起点start都在newInterval end之后的可以直接append
对终点end都在newInterval start之前的都可以append
剩下的就是有交集的，对于end 大于newInterval start的做merge

'''
class Solution3:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        n = len(intervals)

        i = 0
        # intervals completely before
        while i < n and intervals[i][1] < newInterval[0]: 
            res.append(intervals[i])
            i += 1

        # overlapping
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval = [
                min(intervals[i][0], newInterval[0]),
                max(intervals[i][1], newInterval[1])
            ]
            i += 1
        res.append(newInterval)

        # completely after
        while i < n and intervals[i][0] > newInterval[0]:
            res.append(intervals[i])
            i += 1

        return res

'''
思路0
和思路3很像
思路比较巧妙， 不太容易想到
'''
class Solution0:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[1]:
                # intervals是排序过的，意味着剩余的也是start > new end
                res.append(newInterval)
                return res + intervals[i:] #剩余的一次append
            elif intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            else:
                # 注意小技巧是newInterval是不断变化的
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]
        res.append(newInterval) # 最后append merge结果
        
        return res

'''
思路一
在56题的基础上， 把需要insert的interval也看成是需要merge的interval，
加入intervals list，之后merge
时间复杂度O(nlogn)
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intvs = sorted(intervals, key = lambda x:x[0])
        final_intvs = [intvs[0]]

        for i in range(1, len(intvs)):
            # print(final_intvs)
            if intvs[i][0] <= final_intvs[-1][1]:
                final_intvs[-1][1] = max(final_intvs[-1][1], intvs[i][1])
            else:
                final_intvs.append(intvs[i])
                
        return final_intvs

'''
思路二
题目说input interval已经排序过了
‘intervals is sorted in ascending order by starti.’
而且输入已经是non-overlapping intervals
所以不需要额外排序了，只要扫描一遍找到按照starting排序newInterval需要插入的位置插入
之后按照56题思路merge

注意输入intervals可以为空！
'''
class Solution2:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        
        intvs = intervals

        # insert new into intervals by starting order
        for i in range(len(intvs)):
            if intvs[i][0] >= newInterval[0]:
                intvs.insert(i, newInterval)
                break
            elif i == len(intvs) - 1:  # 到最后还没insert，就放在最后end
                intvs.insert(len(intvs), newInterval)
        # print(intvs)

        final_intvs = [intvs[0]]
        for i in range(1, len(intvs)):
            # print(final_intvs)
            if intvs[i][0] <= final_intvs[-1][1]:
                final_intvs[-1][1] = max(final_intvs[-1][1], intvs[i][1])
            else:
                final_intvs.append(intvs[i])
                
        return final_intvs

if __name__ == '__main__':
    s = Solution3()
    print(s.insert([[1,3],[6,9]], [2,5]))
    print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
    print(s.insert([], [2,5]))
    print(s.insert([[1,5]], [2,7]))
    print(s.insert([[1,5]], [6,7]))