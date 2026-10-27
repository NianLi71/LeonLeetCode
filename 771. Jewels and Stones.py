# easy

'''
思路
直接遍历stones，判断每一个stone是否在jewels中
'''


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelsCnt = 0
        for s in stones:
            if s in jewels:
                jewelsCnt += 1

        return jewelsCnt


if __name__ == '__main__':
    s = Solution()

    print(s.numJewelsInStones("aA", "aAAbbbb"))
    print(s.numJewelsInStones("z", "ZZ"))