

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1/self.myPow(x, -n)
        elif n == 0:
            return 1
        else:
            # 重点是这一块做分治，每次处理1/2规模问题，再根据奇偶组合结果
            p = self.myPow(x, n // 2)
            if n % 2 == 0:
                return p*p
            else:
                return p*p*x


if __name__ == '__main__':
    s = Solution()
    print(s.myPow(2.00, 10))
    print(s.myPow(2.1000, 3))
    print(s.myPow(2.000, -2))
