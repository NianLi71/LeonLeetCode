# https://leetcode.com/problems/maximum-product-subarray/


'''
题目大意
计算最大连续子数组的乘积
'''

'''
经典dp题

f[i]保存从0到i最大子数组乘积
f[i] = max(f[i-1]*nums[i], nums[i])
如果乘积还没当前数字大, 就重新开始一个子数组计算

!!!有bug,没有考虑到负负得正的情况
'''
class SolutionBug:
    def maxProduct(self, nums: list[int]) -> int:
        n = len(nums)
        f = [0] * n
        f[0] = nums[0]
        maxP = f[0]
        for i in range(1, n):
            f[i] = max(f[i-1]*nums[i], nums[i])
            maxP = max(maxP, f[i])
        # print(f)
        return maxP


'''
注意和最大连续子数组sum的区别
为了避免负负得正的情况,需要同时保存最大乘积和最小乘积
'''
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n = len(nums)
        f = [0] * n
        g = [0] * n
        f[0] = nums[0]
        g[0] = nums[0]
        maxP = f[0]
        for i in range(1, n):
            pf = f[i-1]*nums[i]
            pg = g[i-1]*nums[i]
            f[i] = max(pf, pg, nums[i])
            g[i] = min(pf, pg, nums[i])
        # print(f)
        return max(max(f), max(g))


if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct([2,3,-2,4]))
    print(s.maxProduct([-2,0,-1]))
    print(s.maxProduct([-2,3,-4]))