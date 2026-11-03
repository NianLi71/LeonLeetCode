# https://leetcode.com/problems/decode-ways/

'''
题目大意
给一串加密过的数字,比如"11106", 加密方式如下
"1" -> 'A'
"2" -> 'B'
...
"25" -> 'Y'
"26" -> 'Z'

计算出有多少种解密方式
For example, "11106" can be decoded into:
"AAJF" with the grouping (1, 1, 10, 6)
"KJF" with the grouping (11, 10, 6)
The grouping (1, 11, 06) is invalid because 
"06" is not a valid code (only "6" is valid).
'''

'''
结论
面试时使用思路二dp和思路三dfs+mem优化即可
'''

'''
思路一
第一想法是dfs枚举所有可能过的解密方式,一旦遇到不合法情况就回退
成功解密完全部数字即结果+1
不需要转换为字母A-Z,直接在数组层面判断
每次枚举1个或2个字符组合,判断是否合法

!!!注意一开始要定义好搜索参数代表什么

整体思路,先dfs,之后剪枝,再思考是否有dp可能

dfs超时,但是从dfs搜索过程可以看出dp基本思路
考虑dfs加记忆mem
'''

'''
这个dfs设计的不太好,
1.中间结果不好复用
2.dfs参数没必要用两个
改进如何复用中间结果
'''
class Solution1:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        validSet = set()
        for i in range(1,27):
            validSet.add(str(i))
        # print(validSet)

        res = 0
        def dfs(i, d):
            # print(i, d)
            # 搜索从i开始d个字符是否合法
            if i + d > n: return
            if i + d == n and s[i:i+d] in validSet:
                nonlocal res
                res += 1
                return
            if s[i:i+d] in validSet:
                dfs(i+d, 1)
                dfs(i+d, 2)

        #从下标0到1个和2个字符开始
        dfs(0, 1)
        dfs(0, 2)
        return res


'''
思路二
dfs超时,但是从dfs搜索过程可以看出dp基本思路
f[i]代表重s[0]到s[i]所有可能decode数量
f[i] = (f[i-1] if s[i] in Set, 0) 
        + (f[i-2] if s[i-1:i-1 + 2], 0)

f[0] = 1 if s[0] in Set
f[1] = (f[0] if s[1] in Set, else 0)
        + (1 if s[1-1:1-1 + 2] in Set, else 0)
f[2] = (f[1] if s[2] in Set, else 0)
        + (f[0] if s[2-1:2-1 + 2] in Set, else 0)


Accepted
Runtime
1ms
Beats
39.22%
'''
class Solution2:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        validSet = set()
        for i in range(1,27):
            validSet.add(str(i))
        # print(validSet)

        if n == 1:
            if s[0] in validSet: return 1
            else: return 0

        f = [0] * n
        f[0] = 1 if s[0] in validSet else 0
        f[1] = (f[0] if s[1] in validSet else 0) \
                + (1 if s[0:2] in validSet else 0)

        for i in range(2,n):
            f[i] = (f[i-1] if s[i] in validSet else 0) \
                + (f[i-2] if s[i-1:i-1 + 2] in validSet else 0)
        # print(f)

        return f[n-1]


'''
思路三
重新设计dfs解法,保存中间结果

分解成子问题, 保存子问题的结果用以加速
递归计算最后结果dfs(n-1)

Runtime
3653ms
Beats
2.16%
'''
class Solution3:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        validSet = set()
        for i in range(1,27):
            validSet.add(str(i))
        # print(validSet)

        mem = [0] * n

        # 计算i可以decode的个数
        def dfs(i):
            # i < 0时, 代表 i >=0 时完全可以decode
            if i < 0: return 1
            if mem[i]:
                return mem[i]

            res = 0
            if s[i] in validSet:
                res += dfs(i-1)
            if i > 0 and s[i-1:i-1 + 2] in validSet:
                # 注意,只有i>0时计算s[i-1:i-1 + 2]才有意思
                res += dfs(i-2)
            mem[i] = res
            return res

        return dfs(n-1)
'''
和思路三基本一样,换成递推,结果dfs(0)
'''
class Solution4:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        validSet = set()
        for i in range(1,27):
            validSet.add(str(i))
        # print(validSet)

        mem = [0] * n

        def dfs(i):
            if i >= n: return 1
            if mem[i]: return mem[i]

            res = 0
            if s[i] in validSet:
                res += dfs(i+1)
            if i + 2 <= n and s[i:i + 2] in validSet:
                res += dfs(i+2)
            mem[i] = res
            return res

        return dfs(0)


if __name__ == '__main__':
    s = Solution3()
    print(s.numDecodings("226"))
    print(s.numDecodings("12"))
    print(s.numDecodings("3"))
    print(s.numDecodings("10"))
    print(s.numDecodings("06"))
    print(s.numDecodings("2101"))
    print(s.numDecodings("1"))
    # # dfs超时
    # print(s.numDecodings("111111111111111111111111111111111111111111111"))
    # print(s.numDecodings("11111111111111111111111111111"))