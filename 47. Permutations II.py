# 递归， dfs

from typing import List

'''
思路一
生成所有排列，对每个排列计算Hash值，每个hash对应的排列只保存一个

思路二
采用排列的递归定义
从i到n个元素排列，第i个元素和i+1 to n的子排列组成一个排列
nums[i] + nums[i+1: n] 
之后一次交换(i, i+1), (i, i+2)...(i, n)重复以上递归排列过程

如果遇到(i, k)数字相等的情况就跳过交换

思路二有bug
对于[2,2,1,1]
因为不是全局去重

还是要加全局hash

'''

'''
思路二 + hash 改进
'''
class Solution1:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        res = []
        def dfs(i, cur):
            if i == n and cur not in res: # hash test
                res.append(cur)
            else:
                for j in range(i, n):
                    if i == j or nums[i] != nums[j]: # i == j 是交换前的一次排列
                        nums[i], nums[j] = nums[j], nums[i]
                        dfs(i+1, cur + [nums[i]])
                        nums[i], nums[j] = nums[j], nums[i]

        dfs(0, [])
        return res


'''
思路二 在改进

对每一位数字，记录它和哪个数组交换过，后续如果再次要交换，就略过
比如[2, 2, 1, 1]
[2_a, 2_b, 1_a, 1_b]
2_a和自己交换过之后， 不会再和2_b交换
2_a和1_a交换后，不会和1_b换
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        res = []
        def dfs(i, cur):
            if i == n:
                res.append(cur)
            else:
                swap_history = []
                for j in range(i, n):
                    if nums[j] in swap_history: #这个判断很关键
                        continue
                    nums[i], nums[j] = nums[j], nums[i]
                    dfs(i+1, cur + [nums[i]])
                    nums[i], nums[j] = nums[j], nums[i]
                    swap_history.append(nums[j])

        dfs(0, [])
        return res

if __name__ == '__main__':
    s = Solution()
    # print(s.permuteUnique([1,1,2]))
    # print(s.permuteUnique([1,2,3]))
    print(s.permuteUnique([2,2,1,1]))