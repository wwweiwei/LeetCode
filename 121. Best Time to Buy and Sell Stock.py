from typing import List
import numpy as np
class Solution():
    def bestTime(self, prices: List[int]) -> int:
        '''
        buy | sell
        define two arrays: 
            min: current minimum
            dp: answer
        '''
        def getdp(n: int) -> int:
            if dp[n] == 999:
                dp[n] = np.maximum(getdp(n-1), prices[n] - min[n-1])
                return dp[n]
            else:
                return dp[n]

        n = int(len(prices))

        min = [999] * n
        dp = [999] * n
        min[0] = prices[0]
        dp[0] = 0

        for i in range(1, n):
            min[i] = np.minimum(prices[i], min[i-1])

        return getdp(n-1)

if __name__ == '__main__':
    sol = Solution()
    ans = sol.bestTime([1,2,3,4,5])
    print(ans)