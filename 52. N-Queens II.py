
'''
这道题和51题基本一样，就是输出是不需要组成board格式，直接输出组合数即可
'''
class Solution:
    def totalNQueens(self, n: int) -> int:

        queues = []
        res = []

        def isValidPosition(p, queues):
            for q in queues:
                if p[0] == q[0] or p[1] == q[1]:
                    return False
                if p[0] + p[1] == q[0] + q[1] or p[1]-p[0] == q[1]-q[0]:
                    return False

            return True


        def dfs(row):
            if row == n:
                # print(queues)
                res.append(queues[:])
                return

            for col in range(n):
                p = (row, col)
                if isValidPosition(p,queues):
                    queues.append(p)
                    # print(queues)
                    dfs(row+1)
                    queues.pop()

        dfs(0) 
        return len(res)

if __name__ == '__main__':
    s = Solution()
    print(s.totalNQueens(4))
    print(s.totalNQueens(1))