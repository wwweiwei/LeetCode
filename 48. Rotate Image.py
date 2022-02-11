from typing import List
class Solution:
    def rotateImage(self, matrix: List[List[int]]) -> List[List[int]]:
        '''
        You have to rotate the image in-place, 
        which means you have to modify the input 2D matrix directly. 
        DO NOT allocate another 2D matrix and do the rotation.
        '''
        # N = len(matrix) # one side
        # for i in range(N//2 + N%2):
        #     for j in range(N//2):
        #         tmp = matrix[i][j] # save temporarily
        #         matrix[i][j] = matrix[-j+(N-1)][i]               # 1
        #         matrix[-j+(N-1)][i] = matrix[-i+(N-1)][-j+(N-1)] # 2
        #         matrix[-i+(N-1)][-j+(N-1)] = matrix[j][-i+(N-1)] # 3
        #         matrix[j][-i+(N-1)]  = tmp  # 4
        # return matrix

        matrix.reverse()
        matrix[:] = list(zip(*matrix))
        return matrix[:]


if __name__ == "__main__":
    sol = Solution()
    ans = sol.rotateImage(matrix = [[1,2,3],[4,5,6],[7,8,9]])
    print(ans)