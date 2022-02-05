from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        dp[i]: minimum number of coins to get i doller
        Initial: set all values as (amount+1) in dp
        Transition: 
            dp[j] = min(dp[j], dp[j-c_value]+1)
        Goal: dp[amount]
        '''
        dp = [(amount+1)] * (amount+1)
        dp[0] = 0
        for j in range(amount+1):
            for _, c_value in enumerate(coins):
                if j-c_value >= 0:
                    dp[j] = min(dp[j], dp[j-c_value]+1)

        if dp[amount] == amount+1:
            return -1
        else:
            return dp[amount]

if __name__ == '__main__':
    sol = Solution()
    ans = sol.coinChange(coins = [1,2,5], amount = 11)
    print(ans)