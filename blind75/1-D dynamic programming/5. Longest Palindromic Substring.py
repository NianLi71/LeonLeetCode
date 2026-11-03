# https://leetcode.com/problems/longest-palindromic-substring/

# 这道题有多种解法，体会不同思路精妙

from pprint import pprint

'''
题目大意
找出最长的回文子字符串
'''

'''
思路一
暴力枚举
1 <= s.length <= 1000
O(n^2*m) m为最长回文子串长度
可能会超时

结果
Runtime
9123ms
Beats
5.01%
'''
class Solution1:
    def longestPalindrome(self, s: str) -> str:
        limit = len(s)

        if limit == 1:
            return s

        def isPalindrome(i, j, s):
            sub = s[i:j+1]
            return sub == sub[::-1]

        start = 0
        end = 0
        maxLen = 0
        for i in range(limit):
            for j in range(i, limit):
                if isPalindrome(i, j, s):
                    if j - i + 1 > maxLen:
                        maxLen = j - i + 1 
                        start = i
                        end = j
                        # print(i, j)
        return s[start:end+1]

'''
思路二
DP动态规划
一个串是回文，等价与该串的首尾字符相等，且去掉首尾后剩下的字符串也是回文

f[i][j]代表s[i..j],包含i,j 是否为回文，True/False

f[i][j] = (s[i] == s[j]) and f[i+1][j-1]
首尾相等，并且中间部分 s[i+1..j-1] 也是回文

如果中间部分为空或者只有 1 个字符，它一定是回文，这时只需要看首尾是否相等：
长度 1（i == j）：一定是回文
长度 2（j == i+1）：只要 s[i] == s[j] 就是回文
长度 3（j == i+2）：中间只有 1 个字符，同样只需 s[i] == s[j]
这三种情况可以合并写成：
dp[i][j] = s[i] == s[j] and (j - i < 3 or dp[i+1][j-1])


枚举顺序很重要
f[i][j] 需要f[i+1][j-1]
i需要递减，j需要递增

Accpeted
Runtime
2682ms
Beats
19.02%
'''
class Solution2:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        f = [ [False] * n for _ in range(n)]

        maxLen = 0
        start = 0
        for i in range(n-1,-1,-1):
            for j in range(i, n):
                if j - i < 3 and s[i] == s[j]:
                    f[i][j] = True
                else:
                    f[i][j] = (s[i] == s[j]) and f[i+1][j-1]
                   
                if f[i][j] == True:
                    if j - i + 1 > maxLen:
                        maxLen = j - i + 1
                        start = i
        # pprint(f)
        # print(start, maxLen)
        return s[start:start+maxLen]

'''
思路三
中心扩展法
每个回文串都有一个中心，而且中心只有两种形式：
奇数长度：中心是 1 个字符，比如 "aba" 的中心是 b
偶数长度：中心是 2 个字符之间的空隙，比如 "abba" 的中心在两个 b 之间

长度为n的字符串，一共有：
n个单字符中心
n-1个空隙中心

枚举中心位置，并向两边拓展

Accepted
Runtime
251ms
Beats
67.01%
'''
class Solution3:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxLen = 0
        start = 0
        for i in range(n):
            # 以一个字符中心
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > maxLen:
                    maxLen = r - l + 1
                    start = l
                l -= 1
                r += 1

            # 以连个字符中间空隙为中心
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > maxLen:
                    maxLen = r - l + 1
                    start = l
                l -= 1
                r += 1

        return s[start:start+maxLen]
            

if __name__ == '__main__':
    s = Solution3()
    print(s.longestPalindrome("babad"))
    print(s.longestPalindrome("b"))
    print(s.longestPalindrome("cbbd"))
    print(s.longestPalindrome("bb"))