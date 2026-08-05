

from dataclasses import dataclass
import string
from typing import List

'''
递归时使用list保存结果

Runtime
0
ms
Beats
100.00%
Memory
19.43
MB
Beats
9.27%
'''
class Solution1:
    def letterCombinations(self, digits: str) -> List[str]:
        m = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        def dfs(i, limit, comb , res):
            if i == limit:
                res.append(''.join(comb))
            else:
                for s in m[digits[i]]:
                    comb.append(s)
                    dfs(i+1, limit, comb , res)
                    comb.pop()

        res = []
        dfs(0, len(digits), [], res)
        # print(res)
        return res

'''
递归时使用string保存结果

Runtime
0
ms
Beats
100.00%
Memory
19.38
MB
Beats
40.07%

'''
class Solution2:
    def letterCombinations(self, digits: str) -> List[str]:
        m = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        def dfs(i, limit, comb , res):
            if i == limit:
                res.append(comb)
            else:
                for s in m[digits[i]]:
                    dfs(i+1, limit, comb+s, res)

        res = []
        dfs(0, len(digits), '', res)
        # print(res)
        return res


'''
非递归使用Stack实现，一般流程是先写出递归版本，
在递归基础上决定Stack保存哪些递归函数需要的参数，
不要一上来就写非递归版本，非递归是优化版本
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        @dataclass(frozen=True)
        class StackItem:
            index: int
            comb: string

        stack = []
        stack.append(StackItem(0, ''))
        limit = len(digits)
        res = []
        while stack:
            # print(f"stack: {stack}")
            item = stack.pop()

            if item.index >= limit:
                res.append(item.comb)
            else:
                for s in m[digits[item.index]]:
                    stack.append(
                        StackItem(item.index + 1, item.comb + s)
                    )

        # print(res)
        return res

if __name__ == '__main__':
    s = Solution()

    s.letterCombinations("2379")