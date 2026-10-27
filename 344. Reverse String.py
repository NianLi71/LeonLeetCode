

'''
思路
s = s[::-1] wont work
需要in-place，不能对s赋值

调换
s[0], s[-1]
s[1], s[-2]
...

s = '12345', n = 5, n//2 = 2, i < 2, i = 0 1
s = '123456', n =6, n//2 = 3, i < 3, i = 0,1,2

'''

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)

        for i in range(n//2):
            last = n-i-1
            # last = -i-1
            t = s[last] # 注意下标
            s[last] = s[i]
            s[i] = t


if __name__ == "__main__":
    s = Solution()

    l = list('12345')
    s.reverseString(l)
    print(l)

    l = list('123456')
    s.reverseString(l)
    print(l)