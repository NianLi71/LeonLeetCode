
'''
模拟题
直接模拟构建二维zigzag，但是忽略空格，忽略不影响结果输出
想象字符串在zigzag第0行和第numRows-1行之间之字形运动，就像小球在两个板之间运动，
在碰到另一个板之前维持运动方向，碰撞后改变方向
忽略空格后，相当于不断保存小球在Y轴上的投影落在哪一行中
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s   # 处理一行的特殊情况

        zigzag = [[] for i in range(numRows)]

        i = 0
        direct = 1
        for e in s:
            zigzag[i].append(e) # 不去管空格，直接一个接一个append就行
            if i == 0: # 出发时或者是回到了zigzag最上一行，此时应该往下走
                direct = 1
            elif i == numRows - 1: # 到达zigzag最下行，应该掉头往上走 
                direct = -1

            i = i + direct
        # print(zigzag)

        res = ""
        for row in zigzag:
            res = res + ''.join(row)
        
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.convert("PAYPALISHIRING", 3))
    print(s.convert("PAYPALISHIRING", 4))
    print(s.convert("A", 1))
    print(s.convert("AB", 1))
    print(s.convert("ABC", 1))