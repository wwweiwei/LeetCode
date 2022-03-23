class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return 
        n, m = len(board), len(board[0])
        
        # 找出所有的邊界O，將其押入棧中
        stack = []
        for i in range(n):
            for j in range(m):
                if ((i in (0, n - 1)) or (j in (0, m - 1))) and board[i][j] == 'O':
                    stack.append((i, j))
        
        # 標記所有能聯絡到邊界的O的O
        while stack:
            r,c = stack.pop(0)
            
            if 0<=r<n and 0<=c<m and board[r][c] == 'O':
                board[r][c] = 'M'
                if r-1>=0 and board[r-1][c] == 'O':
                    stack.append((r-1,c))
                if r+1<n and board[r+1][c] == 'O':
                    stack.append((r+1,c))
                if c-1>=0 and board[r][c-1] == 'O':
                    stack.append((r,c-1))
                if c+1<m and board[r][c+1] == 'O':
                    stack.append((r,c+1))
        
        # 更新
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'M':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
                    