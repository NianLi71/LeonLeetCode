# 递归， dfs

from typing import List

'''
思路一
递归，同时记录哪个数字被使用过了，下一位数字只能使用其他数字

Accepted
'''
class Solution1:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        used = set()

        def dfs(d, cur):
            if d == n:
                res.append(cur[:])
            else:
                for i in nums:
                    if i not in used:
                        used.add(i)
                        dfs(d+1, cur + [i])
                        used.remove(i)

        dfs(0, [])

        return res

'''
思路二
递归定义更严谨
一个排列递归定义为
num[0]+余下数字的排列
交换index=k的数组与index=0
num[k]+余下数字的排列

Accepted
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def swap(i, j, n):
            n[i], n[j] = n[j], n[i]

        def dfs(n, cur):
            if not n: #没有余下数字了
                res.append(cur[:])
            else:
                for i in range(len(n)):
                    swap(0, i, n)
                    dfs(n[1:], cur + [n[0]]) # 固定第一个数字+余下数字全排列
                    swap(0, i, n)
            

        dfs(nums, [])

        return res

if __name__ == '__main__':
    s = Solution()
    print(s.permute([1,2,3]))
    print(s.permute([1,2]))
    print(s.permute([1]))