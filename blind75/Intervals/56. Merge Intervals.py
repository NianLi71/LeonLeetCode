# https://leetcode.com/problems/merge-intervals/



from typing import List


'''
思路
对所有interval按照起点升序排列
之后依次merge, 判断下一个interval是否和已经merged的最后一个interval有交集，
因为已经按照起点排序过了，所以每次只用和最后一个计算是否merge
final_intvs中保存都是merge过没法再merge的intervals
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intvs = sorted(intervals, key = lambda x:x[0])
        final_intvs = [intvs[0]]

        for i in range(1, len(intvs)):
            # print(final_intvs)
            if intvs[i][0] <= final_intvs[-1][1]:
                final_intvs[-1][1] = max(final_intvs[-1][1], intvs[i][1])
            else:
                final_intvs.append(intvs[i])
                
        return final_intvs

if __name__ == '__main__':
    s = Solution()
    print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
    print(s.merge([[1,4],[4,5]]))
    print(s.merge([[4,7],[1,4]]))
    print(s.merge([[4,7]]))