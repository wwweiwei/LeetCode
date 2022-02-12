from typing import List
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        '''
        Brute force: 
            Method: go through all the grid 
                    and determine whether id negative
            Time complexity: n^2
            
        Optimal:
            Method: use binary search to find the first negative number
            Time complexity: nlogn
        '''
        ## Brute force
        # cnt = 0
        # for row, v in enumerate(grid):
        #     for element in grid[row]:
        #         if element < 0:
        #             cnt += 1
        # return cnt

        ## binary search
        # def binary_search(row, start, end):
        #     if start == end:
        #         if row[start] < 0:
        #             return start
        #         else:
        #             return len(row)

        #     middle = (start+end) // 2
        #     if row[middle] < 0 and middle == 0:
        #         return 0
        #     elif row[middle] < 0 and row[middle-1] >= 0:
        #         return middle

        #     if row[middle] >= 0:
        #         return binary_search(row, middle+1, end)
        #     else:
        #         return binary_search(row, start, middle-1)

        # cnt = 0
        # for row in grid:
        #     if row != []:
        #         first_neg_id = binary_search(row, 0, len(row)-1)
        #         cnt += int(len(row)-int(first_neg_id))
        # return cnt

        ## method
        cnt = 0
        m = len(grid) # row
        n = len(grid[0]) # col
        i = m-1
        j = 0
        while i >= 0 and j < n:
            if grid[i][j] < 0:
                cnt += n-j
                i -= 1
                # j = 0
            else:
                j += 1
                
        return cnt

if __name__ == "__main__":
    sol = Solution()
    ans = sol.countNegatives(grid = [[3,-1,-3,-3,-3],[2,-2,-3,-3,-3],[1,-2,-3,-3,-3],[0,-3,-3,-3,-3]])
    print(ans)