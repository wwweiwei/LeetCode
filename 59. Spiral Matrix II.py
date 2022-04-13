class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return []
        
        ans = [[0 for col in range(n)] for row in range(n)]
        ans[0][0] = 1
        
        cnt, direction = 1, 0
        i, j = 0, 0
        weight = 1
        
        while cnt < n * n:
            if direction == 0:
                j += 1
                ans[i][j] = cnt + 1
                if j == n - weight:
                    direction = 1
            elif direction == 1:
                i += 1
                ans[i][j] = cnt + 1
                if i == n - weight:
                    direction = 2
            elif direction == 2:
                j -= 1
                ans[i][j] = cnt + 1
                if j == weight - 1:
                    direction = 3
                    weight += 1
            elif direction == 3:
                i -= 1
                ans[i][j] = cnt + 1
                if i == weight - 1:
                    direction = 0
            cnt += 1
        return ans
        