# https://leetcode.com/problems/longest-substring-without-repeating-characters/


'''
思路
维护一个只包含unqiue字符的窗口 [l,r]
每次往右遍历移动一次r
如果s[r]和窗口中已有字符重复，就不断右移l, 同时从unique set中remove s[l], 直到s[r]在charSet中是unique
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        maxLen = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            maxLen = max(maxLen, r - l + 1)
        return maxLen