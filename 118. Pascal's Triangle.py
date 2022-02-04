from typing import List
class Solution:
    def pascalsTriangle(self, numRows: int) -> List[List[int]]:
        '''
        E.g. 
            Input: numRows = 5
            Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
        if j == 0:
            ans[i][j] = ans[i-1][j]
        elif j == i:
            ans[i][j] = ans[i-1][j-1]
        else:
            ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
        '''
        ans = []
        ans.append([1])
        for i in range(1, numRows):
            l = []
            for j in range(i+1):
                if j == 0:
                    l.append(ans[i-1][j])
                elif j == i:
                    l.append(ans[i-1][j-1])
                else:
                    l.append(ans[i-1][j-1] + ans[i-1][j])
            ans.append(l)
        return ans

if __name__ == '__main__':
    sol = Solution()
    ans = sol.pascalsTriangle(5)
    print(ans)