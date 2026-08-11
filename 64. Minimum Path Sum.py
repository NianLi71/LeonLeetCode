# 动态规划

'''
这题和62,63题很像，
动态规划计算最小路径

f[i][j] = min(f[i-1][j], f[i][j-1]) + g[i][j]
f[0][0] = g[0][0]
'''
from typing import List

'''
Accepted
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        f = [ [0]*n for _ in range(m) ]
        for i in range(m):
            for j in range(n):
                if i ==0 and j ==0:
                    f[0][0] = grid[0][0]
                elif i -1 < 0:
                    f[i][j] = f[i][j-1] + grid[i][j]
                elif j - 1< 0:
                    f[i][j] = f[i-1][j] + grid[i][j]
                else:
                    f[i][j] = min(f[i-1][j], f[i][j-1]) + grid[i][j]

        return f[m-1][n-1]

if __name__ == '__main__':
    s = Solution()
    print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
    print(s.minPathSum([[1,2,3],[4,5,6]]))