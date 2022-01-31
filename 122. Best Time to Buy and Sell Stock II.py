from typing import List
class Solution:
    def bestTime(self, prices: List[int]) -> int:
        '''
        Goal: Sum the maximum profits
        Method:
            Find any increasing pattern
        '''
        last_day = prices[0]
        total = 0
        for _,v in enumerate(prices):
            if v>last_day:
                total += (v-last_day)
            last_day = v
        return total 
if __name__ == '__main__':
    sol = Solution()
    ans = sol.bestTime([1,2,3,4,5])
    print(ans)