# 动态规划

'''
这题和62题很像，就是有计算时有障碍的格子f[i][j] = 0
后续继续即可

Accepted
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        f = [[0] * n for _ in range(m)]

        def path(i, j):
            if i < 0 or j < 0: return 0
            return f[i][j]

        for i in range(m):
            for j in range(n):
                if i ==0 and j==0:
                    if obstacleGrid[0][0] == 1: return 0
                    else:
                        f[0][0] = 1
                elif obstacleGrid[i][j] == 1:
                    f[i][j] = 0
                else:
                    f[i][j] = path(i-1, j) + path(i,j-1)

        return f[m-1][n-1]


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
    print(s.uniquePathsWithObstacles([[0,1],[0,0]]))
    print(s.uniquePathsWithObstacles([[1],[0]]))