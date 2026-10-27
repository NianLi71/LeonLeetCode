# esay

'''
思路
枚举每个可以删除的位置，并比较删除后数字的大小
不需要转为数字，str可以直接比较
'''

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        maxNumber = '0'
        for i in range(len(number)):
            if number[i] == digit:
                n = number[0:i] + number[i+1:]
                # print(n)
                if n > maxNumber:
                    maxNumber = n
        return maxNumber

if __name__ == '__main__':
    s = Solution()
    print(s.removeDigit('123', '3'))
    print(s.removeDigit('1231', '1'))
    print(s.removeDigit('551', '5'))