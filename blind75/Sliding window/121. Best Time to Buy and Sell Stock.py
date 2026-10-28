# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


'''
思路
遍历的同时记录到今天之前的最低价格
并计算到今天的收益，决定是否更新maxGain
'''

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minPrice = prices[0]
        maxGain = 0
        for p in prices:
            gain = p - minPrice # gain = 当天的价格减去今天之前的最低价格
            maxGain = max(maxGain, gain)
            minPrice = min(minPrice, p) 
        return maxGain

if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
    print(s.maxProfit([7,6,4,3,1]))