class Solution:
    def solveNQueens(self, n):
        res = []
        grid = [['.'] * n for i in range(n)]
        cols, diag1, diag2 = [0] * n, [0] * (2 * n - 1), [0] * (2 * n - 1)
        def mark(i,j, on=True):
            m = (1 if on else 0)
            cols[j], diag1[i+j], diag2[n-1-i+j] = m, m, m
            grid[i][j] = ('Q' if on else '.')

        def valid(i, j):
            return not cols[j] and not diag1[i+j] and not diag2[n-1-i+j] and grid[i][j] == '.'

        def dfs(row):
            if row >= n:
                res.append([''.join(x) for x in grid])
            else:
               for i in range(n):
                   if valid(row, i):
                       mark(row, i)
                       dfs(row+1)
                       mark(row, i, False)
        dfs(0)
        return res

s = Solution()
print(s.solveNQueens(10))