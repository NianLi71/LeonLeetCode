

'''
用stack模拟，遇到左括号入栈，遇到右括号出栈比较是否配对，右括号不入栈
注意几个边界条件

Runtime
3
ms
Beats
32.08%
Memory
19.16
MB
Beats
91.18%
'''
class Solution:
    def isValid(self, s: str) -> bool:
        # 对右括号保存它的左括号匹配，方便快速查询配对
        pair = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []
        for c in s:
            if c not in pair: # 是左括号
                stack.append(c)
            else: 
                if not stack: # 注意边界条件！只有一个 ']'的情况，此时stack为空，pop会报错. 右括号来了但是stack没有任何括号
                    return False
                last = stack.pop()
                if last != pair[c]:
                    return False

        # 注意边界情况，stack不为空，[([]), 最后会剩一个左括号
        if stack:
            return False
        return True
        
if __name__ == '__main__':
    s = Solution()
    print(s.isValid(')'))