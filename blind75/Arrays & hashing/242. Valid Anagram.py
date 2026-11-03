# https://leetcode.com/problems/valid-anagram/


'''
题目大意
给定两个字符串s,t
能否使用全部s中的每个字符一次重组成字符串t,
注意是全部并且有且仅用一次
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = list(s)
        a.sort()

        b = list(t)
        b.sort()

        return ''.join(a) == ''.join(b)

        # Or one line
        # return ''.join( sorted(list(s)) ) == ''.join( sorted(list(t)))


if __name__ == "__main__":
    s = Solution()
    print(s.isAnagram(s = "anagram", t = "nagaram"))
    print(s.isAnagram(s = "rat", t = "car"))