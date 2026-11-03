# https://leetcode.com/problems/encode-and-decode-strings/
# https://neetcode.io/problems/string-encode-and-decode/solution

from typing import List


class Solution:
    tag = '#'
    debug = False
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append(Solution.tag)
            res.append(s)
        if Solution.debug: print(res)
        encodedStr = ''.join(res)
        if Solution.debug: print(encodedStr)
        return encodedStr


    def decode(self, s: str) -> List[str]:
        limit = len(s)
        i = 0
        res = []
        while i < limit:
            j = i + 1
            while j < limit and s[j] != Solution.tag:
                j += 1
            sLen = int(s[i:j])
            res.append(s[j+1:j+1 + sLen])
            i = j + 1 + sLen
            if Solution.debug: print(sLen, s[j+1:sLen])
        if Solution.debug: print(res)
        return res


if __name__ == '__main__':
    s  = Solution()

    input = ["Hello","World"]
    output = s.decode(s.encode(input))
    assert input == output, f'{input}, {output}'

    input = [""]
    output = s.decode(s.encode(input))
    assert input == output

    input = ["", ""]
    output = s.decode(s.encode(input))
    assert input == output