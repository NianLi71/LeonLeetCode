

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:

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

        def formatOutput(res):
            finalRes = []
            for r in res:
                board = [['.'] * n for _ in range(n)] 
                for q in r:
                    board[q[0]][q[1]] = 'Q'

                for row in range(n):
                #     # s = ''
                #     # for col in range(n):
                #     #     s += board[row][col]
                    board[row] = ''.join(board[row]) # 简洁版

                # board = [ ''.join(board[row]) for row in range(n)] # 更简洁
                finalRes.append(board)
            return finalRes

        dfs(0) 
        return formatOutput(res)

if __name__ == '__main__':
    s = Solution()
    print(s.solveNQueens(4))