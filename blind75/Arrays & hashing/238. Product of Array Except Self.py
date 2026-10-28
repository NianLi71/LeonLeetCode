# https://leetcode.com/problems/product-of-array-except-self/


'''
题目的意思是，计算数组中除了自己之外，其余所有元素的乘积
要在O(n)计算，不能用除法
'''

'''
思路一：
对每个数字，从左右分别计算包含当前数字的乘积：
input: [1,2,3,4]
fromLeft: [1, 2, 6, 24]
fromRgith:[24, 24, 12, 4]

input: [-1,1,0,-3,3]
fromLeft: [-1, -1, 0, 0, 0]
fromRgith:[0, 0, 0, -9, 3]

之后做一次遍历，
fromLeft[i-1]为从左边过来的乘积，
fromRight[i+1]为从右边过来的乘积，
以上均不包含nums[i],
计算fromLeft[i-1] * fromRight[i+1]作为结果，
注意处理边界情况
'''
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        limit = len(nums)
        fromLeft = []
        for i in range(limit):
            if i == 0:
                fromLeft.append(nums[i])
            else:
                fromLeft.append(fromLeft[-1]*nums[i])

        fromRight = []
        for i in range(limit-1,-1,-1):
            if i == limit-1:
                fromRight.append(nums[i])
            else:
                fromRight.append(fromRight[-1]*nums[i])
        fromRight.reverse()

        # print(fromLeft)
        # print(fromRight)

        res = []
        for i in range(limit):
            if i == 0:
                res.append(fromRight[i+1])
            elif i == limit - 1:
                res.append(fromLeft[i-1])
            else:
                res.append(fromLeft[i-1] * fromRight[i+1])

        return res

'''
思路二：
在思路一的基础上，整体思路不变，优化一些逻辑
记录当前位置的不包含当前数字的前缀乘积pre,和后缀乘积suff
pre[0] = suff[n-1] = 1
'''
class Solution2:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        pre = [0] * n
        suff = [0] * n
        res = [0] * n
        pre[0] = suff[n-1] = 1

        for i in range(1, n):
            pre[i] = pre[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            suff[i] = suff[i+1] * nums[i+1]
        # print(pre)
        # print(suff)
        for i in range(n):
            res[i] = pre[i]*suff[i]

        return res

'''
思路三
思路一二都是 time&space complexity O(n)
思路三把space降到O(1)
'''
class Solution3:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n

        pre = 1
        for i in range(n):
            res[i] = pre
            pre *= nums[i]
        suff = 1
        for i in range(n-1,-1,-1):
            res[i] *= suff
            suff *= nums[i]

        return res


if __name__ == '__main__':
    s = Solution3()
    print(s.productExceptSelf([1,2,3,4]))
    print(s.productExceptSelf([-1,1,0,-3,3]))