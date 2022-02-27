class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        Given an m x n 2D binary grid grid 
        which represents a map of '1's (land) 
        and '0's (water), return the number of islands.
        '''
        
        visited = set()
        count = 0
        row = len(grid)
        col = len(grid[0])
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        def dfs(i, j):
            for x, y in direction:
                if 0<=i+x<row and 0<=j+y<col and grid[i+x][j+y] == "1" and (i+x, j+y) not in visited:
                    visited.add((i+x, j+y))
                    dfs(i+x, j+y)
                    
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i, j) not in visited:
                    count += 1
                    visited.add((i, j))
                    dfs(i, j)
        return count

if __name__ == "__main__":
    sol = Solution()
    ans = sol.numIslands(grid = [
                    ["1","1","1","1","0"],
                    ["1","1","0","1","0"],
                    ["1","1","0","0","0"],
                    ["0","0","0","0","0"]
                    ])
    print(ans)