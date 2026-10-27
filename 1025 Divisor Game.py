
'''
思路一
Alice先手，题目就是判断给定一个n，先手能否取胜
思路Alice如果要赢，就是要先手动一步让Bob后手必败
第一列n, 第二列can Alice win?
n=1, lose
n=2, win, Alice chooses 1, then Bob at n=1 loses
n=3, lose, Alice chooses 1, then Bob at n=2, Bob wins
n=4, win, Alice chooses 1, then Bob at n=3, Bob loses
n=5, lose, Alice can only chooses 1,
n=6, win, Alice can chooses 1,2,3, Alice can choose 3 to win
n=7, lose, 7-1=6
n=8, win, 8-1=7
n=9, lose
n=10, win, 10-1=9
n=11, lose
n=12, win
n=13, lose
n=14, win
n=15, lose
n=16, win
n=17, lose
n=18, win
n=19, lose
n=20, win
n=21, lose

能否得出结论奇数必输?
奇数的因子是奇数，奇数-奇数等于偶数，后手偶数必胜

Accepted


思路二：
递推，模拟我上面的操作，递推到结果n
'''

class Solution:
    def divisorGame(self, n: int) -> bool:
        if n % 2 == 0:
            return True
        else:
            return False


class Solution2:
    def divisorGame(self, n: int) -> bool:
        f = [False] * (n+1)
        for i in range(2, n+1):
            for j in range(1, int(i**0.5)+1):
                if i % j == 0:
                    if f[i-j] == False:
                        f[i] = True
                        break
                        
        # print(f[1:])
        return f[n]

if __name__ == '__main__':
    s = Solution2()
    # print(s.divisorGame(1))
    # print(s.divisorGame(2))
    # print(s.divisorGame(3))
    # print(s.divisorGame(4))
    # print(s.divisorGame(5))
    # print(s.divisorGame(20))
    print(s.divisorGame(21))