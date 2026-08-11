# 动态规划


'''
思路一
一上来就想用搜索做，写出来后发现运行很慢， 会超时

思路二
动态规划！
好久没做题都忘了！

'''


'''
纯搜索的话会超时
'''
class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        dir = [(1,0), (0,1)] #only move down or right
        sx = 0
        sy = 0

        pathCount = 0

        def isValid(x, y):
            if x < 0 or x >= m or y < 0 or y >= n:
                return False
            return True

        def dfs(x, y):
            nonlocal pathCount
            if isValid(x,y):
                if x == m-1 and y == n-1:
                    pathCount += 1
                    return
            
                for d in dir:
                    dfs(x+d[0], y+d[1])

        dfs(sx, sy)
        return pathCount

'''
动态规划！
f[0][0] = 1
f[i][j] = f[i-1][j] + f[i][j]
边界外 f[i][j] = 0
return f[m-1][n-1]
 
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        g = [ [0] * n for i in range(m)] #构造二维数组
        # 笨办法构造也可以
        # 1.
        # k = []
        # for i in range(m):  m行
        #     k.append([0] * n ) n列
        # 2.
        # k = []
        # for i in range(3):
        #     l = []
        #     for j in range(2):
        #         l.append(0)
        #     k.append(l)

        def pathCount(i, j):
            if i < 0 or j < 0:
                return 0
            return g[i][j]

        for i in range(0, m):
            for j in range(0, n):
                if i == 0 and j == 0:
                    g[i][j] = 1
                else:
                    g[i][j] = pathCount(i-1, j) + pathCount(i, j-1)

        return g[m-1][n-1]

'''
动态规划二
也可以用if判断处理边界
'''
class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        if m*n == 0:
            return 0
        grid = [ [0]*m for i in range(n)]
        grid[0][0] = 1
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                elif i - 1 < 0:
                    grid[i][j]= grid[i][j-1]
                elif j - 1 < 0:
                    grid[i][j]=grid[i-1][j]
                else:
                    grid[i][j] = grid[i-1][j]+grid[i][j-1]
        return grid[n-1][m-1]


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(3,7))
    print(s.uniquePaths(3,2))
    print(s.uniquePaths(100,100))