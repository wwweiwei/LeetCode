from typing import List
class Solution:
    def coinChange(self, amount: int, coins: List[int]) -> int:
        '''
        Return the number of combinations that make up that amount. 
        If that amount of money cannot be made up by any combination of the coins, return 0.
        '''
        dp = [0] * (amount+1)
        dp[0] = 1
        for _, c_value in enumerate(coins):
            for j in range(1, amount+1):
                if j - c_value >= 0:
                    dp[j] += dp[j-c_value]

        return dp[amount]

if __name__ == '__main__':
    sol = Solution()
    ans = sol.coinChange(amount = 5, coins = [1,2,5])
    print(ans)