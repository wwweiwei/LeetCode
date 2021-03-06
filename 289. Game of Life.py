class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        d = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        for i in range(m):
            for j in range(n):
                live = 0
                for tx, ty in d:
                    x, y = i + tx, j + ty
                    if x < 0 or x == m or y < 0 or y == n:
                        continue
                    if board[x][y] & 1:
                        live += 1
                if board[i][j] == 0:
                    if live == 3:
                        board[i][j] = 2
                else:
                    if 2 <= live <= 3:
                        board[i][j] = 3
                    else:
                        board[i][j] = 1

        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1

        # direction = [(1, 0), (-1, 0), (0, 1), 
        #              (0, -1), (-1, -1), (-1, 1), 
        #              (1, -1), (1, 1)]
        
        # if board is None:
        #     pass
        # else:
        #     ans = board
            
        #     for row in range(len(board)):
        #         for col in range(len(board[0])):
        #             neighbor = 0
        #             for i, j in direction:
        #                 x, y = row+i, col+j
        #                 if 0 <= x < len(board) and 0 <= y < len(board[0]):
        #                     neighbor += board[x][y]
                            
        #             if board[row][col] == 1 and neighbor < 2:
        #                 ans[row][col] = 0
        #             elif board[row][col] == 1 and neighbor > 3:
        #                 ans[row][col] = 0
        #             elif board[row][col] == 0 and neighbor == 3:
        #                 ans[row][col] = 1
                        
        #     for row in range(len(board)):
        #         for col in range(len(board[0])):
        #             board[row][col] = ans[row][col]
                            