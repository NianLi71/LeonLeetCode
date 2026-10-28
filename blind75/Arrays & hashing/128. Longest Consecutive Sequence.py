# https://leetcode.com/problems/longest-consecutive-sequence/


'''
思路
结果需要时连续的数字，相邻之间相差1
对nums构建set
为了避免重复计算每个longest seq, 对每个num, 先判断num-1是否在set中，
如果不在，说明num是一个seq的开头，之后依次判断num+1, num+2,...是否在set中
统计从num开始的longest seq len，记录最长的

'''

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numsSet = set(nums)
        maxLen = 0

        for n in numsSet: # 只在set中遍历
            if n - 1 not in numsSet:
                length = 1
                while n + length in numsSet:
                    length += 1
                maxLen = max(maxLen, length)

        return maxLen

if __name__ == '__main__':
    s = Solution()

    print(s.longestConsecutive([100,4,200,1,3,2]))
    print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
    print(s.longestConsecutive([1,0,1,2]))
    print(s.longestConsecutive([]))