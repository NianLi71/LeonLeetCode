

'''
思路
看起来周长不好算，仔细一分析，遍历每个island方块
发现只要对每个小方块计算四个方向是否有水，如果有水就周长+1

'''


class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        dirs = ((0,1),(0,-1),(-1,0),(1,0))
        perimeter = 0

        rowLimit = len(grid)
        colLimit = len(grid[0]) # 1 <= row, col <= 100

        def isInGrid(i, j):
            if i < 0 or i >= rowLimit: return False
            if j < 0 or j >= colLimit: return False
            return True

        def getPerimeter(i, j): # 对一个小格子计算周长
            p = 0
            for d in dirs:
                iNext = i+d[0]
                jNext = j+d[1]
                # 到边界了或者与水相邻
                if not isInGrid(iNext, jNext) or isInGrid(iNext, jNext) and grid[iNext][jNext] == 0:
                    p += 1
            return p

        for i in range(rowLimit):
            for j in range(colLimit):
                if grid[i][j] == 1:
                    perimeter += getPerimeter(i, j)

        return perimeter


if __name__ == "__main__":
    s = Solution()
    print(s.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
    print(s.islandPerimeter([[1]]))
    print(s.islandPerimeter([[1, 0]]))
    print(s.islandPerimeter([[0, 0]]))