from typing import List
import numpy as np
class Solution:
    def validSudoku(self, board: List[List[str]]) -> bool:
            '''
            Check if the same row, same col and same block have number duplicate
            Solution: use dict
                (i, -1, num): row
                (-1, j, num): col
                (i, j, num): block
            '''
            dict1 = {}
            for i in range(9):
                for j in range(9):
                    if board[i][j] != '.':
                        num = int(board[i][j])
                        if (i, -1, num) in dict1 or (-1, j, num) in dict1 or (i//3, j//3, num) in dict1:
                            return False
                        dict1[(i, -1, num)] = True
                        dict1[(-1, j, num)] = True
                        dict1[(i//3, j//3, num)] = True
            return True

if __name__ == "__main__":
    sol = Solution()
    ans = sol.validSudoku(board = 
            [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]])
    print(ans)