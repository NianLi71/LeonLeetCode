
'''
Convert to string

Runtime
3
ms
Beats
88.88%
Memory
19.23
MB
Beats
54.11%

'''
class Solution1:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        return False

'''
convert to list then compare
'''
class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False
        elif x == 0:
            return True

        # convert to list
        l = []
        while x:
            l.append(x % 10)
            x = x // 10

        return l == l[::-1]

'''
Build reverse number
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False
        elif x == 0:
            return True

        rev_x = 0
        xx = x
        while x:
            rev_x = x % 10 + rev_x * 10
            x = x // 10
        print(rev_x, xx)

        return rev_x == xx




if __name__ == '__main__':
    s = Solution()

    r = s.isPalindrome(10132)
    print(r)