
'''
递推
先手推了下n = 4
1,1,1,1
1,1,2
1,2,1
2,1,1
2,2

后来意识到, 用f[n]代表跳到n需要多少步：
f[4] = f[2] + f[3]
从2跳2步到4
从3跳1步到4
所以跳到4的步数总和等于f[2] + f[3]

'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        f = [0]*(n+1)
        f[1] = 1
        f[2] = 2
        for i in range(3, n+1):
            f[i] = f[i-1] + f[i-2]

        return f[n]

if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(1))
    print(s.climbStairs(2))
    print(s.climbStairs(3))
    print(s.climbStairs(4))
    print(s.climbStairs(45))