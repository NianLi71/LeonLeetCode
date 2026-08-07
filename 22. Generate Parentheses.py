# 递归


from typing import List

'''
Runtime
1
ms
Beats
41.60%
Memory
19.39
MB
Beats
72.40%

'''
class Solution1:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        def dfs(i, limit, lc, rc, comb): # lc做括号数，lr右括号数
            if lc > n or rc > n or rc > lc: # invalid comb
                return
            if i > limit: # 生成2*n个括号就停止
                res.append(comb)
                return

            # 先生成，在下一层判断是否合理
            dfs(i+1, limit, lc+1, rc, comb+'(')
            dfs(i+1, limit, lc, rc+1, comb+')')
            
        dfs(1, n * 2, 0, 0, '')

        return res

'''
小优化版本
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        def dfs(i, lc, rc, comb): # lc做括号数, rc右括号数
            if lc > n or rc > n or rc > lc: # invalid comb
                return
            if rc == n: # 这里可以小优化一下，停止条件是判断右括号数正好等于n
                res.append(comb)
                return

            # 先生成，在下一层判断是否合理
            dfs(i+1, lc+1, rc, comb+'(')
            dfs(i+1, lc, rc+1, comb+')')
            
        dfs(1, 0, 0, '')

        return res

if __name__ == '__main__':
    s = Solution()

    print(s.generateParenthesis(3))