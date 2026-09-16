

'''
f[0] = 0
f[i, k] = {
            f[i] + 1, if f[i+k] == 0;
            min(f[i+k], f[i] + 1), if f[i+k] != 0
            }
可以把f[i] 初始化为math.inf, 可以简化计算

速度稍慢3692ms，可以accepted
思路清晰
'''
class Solution1:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        f = [0] * n

        for i in range(n):
            for k in range(1, nums[i]+1):
                if i + k < n:
                    if f[i+k] == 0:
                        f[i+k] = f[i]+1
                    else:
                        f[i+k] = min(f[i+k], f[i]+1)
        # print(f)
        return f[-1]

'''
速度优化版本，但是没想清楚why
'''
class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        r, c, l =0,0,0

        for i in range(n-1):
            r = max(r, i+nums[i])
            if i == l:
                l = r
                c += 1
        return c

if __name__ == '__main__':
    s = Solution()
    print(s.jump([2,3,1,1,4]))
    print(s.jump([2,3,0,1,4]))
    print(s.jump([2,3,1,1,1,4]))