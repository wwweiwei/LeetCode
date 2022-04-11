class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        if grid is None:
            return grid
        
        num_row = len(grid)
        num_col = len(grid[0])

        ans = [[0]*num_col for i in range(num_row)]
        k %= (num_row*num_col)
        
        for i in range(num_row):
            for j in range(num_col):
                index = i*num_col + j
                index += k
                index %= (num_row*num_col)
                ans[index/num_col][index%num_col] = grid[i][j]
        
        return ans
        