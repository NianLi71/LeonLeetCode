

'''
有些tricky, 思路见注释
'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        curMaxLength = 0 # 到目前索引位置上有效的最大长度
        maxLength = 0
        for i, c in enumerate(s):
            if c == '(': #只有左括号入栈
                # 入栈保存：目前到这个左括号时，左边连续有效的括号最大长度
                # 如果一个有效右括号后面是一个左括号，那么此时curMaxLength就不为0
                stack.append([i, curMaxLength]) # 可选保存index
                curMaxLength = 0 # 因为当前索引位置是左括号，还没有右匹配，所以重置为0
            else: #是右括号
                if len(stack) == 0: # 但是没有左括号匹配
                    curMaxLength = 0 # 到目前这个右括号，没有有效长度，重置为0
                else: # 有对应的左括号匹配
                    _, validLengthSoFar = stack.pop()
                    # 更新目前有效最大长度
                    curMaxLength += validLengthSoFar + 2  # +2 是因为当前右括号匹配栈里左括号，长度加2
                    maxLength = max(maxLength, curMaxLength)

        return maxLength

if __name__ == '__main__':
    s = Solution()
    print(s.longestValidParentheses("(()"))
    print(s.longestValidParentheses(")()())"))
    print(s.longestValidParentheses(""))