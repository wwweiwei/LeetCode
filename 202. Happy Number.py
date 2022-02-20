from typing import List
import numpy as np
class Solution:
    def isHappy(self, n: int) -> bool:
        ans = n
        count = 0
        while ans != 1:
            count += 1
            n_str = list(str(ans))
            numbers = [int(x)**2 for x in n_str]
            ans = sum(numbers)
            if count >= 100:
                return False
        return True

if __name__ == "__main__":
    sol = Solution()
    ans = sol.isHappy(7)
    print(ans)