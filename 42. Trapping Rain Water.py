

class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        maxLeftHeight = [0] * n
        maxRightHeight = [0] * n

        # 计算每个bar对应左边最高的高度
        curMaxLeftHeight = 0
        for i, h in enumerate(height):
            if h > curMaxLeftHeight:
                curMaxLeftHeight = h
            maxLeftHeight[i] = curMaxLeftHeight
        # print(maxLeftHeight)

        # 同样计算每个bar右边最高的高度，从右往左计算
        curMaxRightHeight = 0
        for i in range(n-1, -1, -1):
            if height[i] > curMaxRightHeight:
                curMaxRightHeight = height[i]
            maxRightHeight[i] = curMaxRightHeight
        # print(maxRightHeight)

        totalWater = 0
        for i in range(n):
            # 取左右最低高低减去当前bar高度
            water = min(maxLeftHeight[i], maxRightHeight[i]) - height[i]
            if water > 0:
                totalWater += water

        return totalWater


if __name__ == '__main__':
    s = Solution()
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(s.trap([4,2,0,3,2,5]))
    print(s.trap([0]))