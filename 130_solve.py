class Solution:
    def __init__(self):
        self.directions = [(-1,0), (0,1), (1,0), (0,-1)]

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not len(board): return []
        m,n = len(board), len(board[0])
        marked = [[False]*n for _ in range(m)]
        for i in [0, m-1]:
            for j in range(n):
                if board[i][j] == 'O':
                    marked[i][j] = True
                    self.search(i, j, marked, m, n, board)

        for j in [0, n-1]:
            for i in range(m):
                if board[i][j] == 'O':
                    marked[i][j] = True
                    self.search(i, j, marked,m,n, board)
        
        for i in range(m):
            for j in range(n):
                if marked[i][j]:
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'

    def search(self, x, y, marked, m, n, board):
        for direction in self.directions:
            new_x, new_y = x+direction[0], y+direction[1]
            if 0<=new_x<=m-1 and 0<=new_y<=n-1 and board[new_x][new_y] == 'O' and \
                not marked[new_x][new_y]:
                marked[new_x][new_y] = True
                self.search(new_x, new_y, marked, m, n, board)
