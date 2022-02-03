from typing import List
import numpy as np
class Solution:
    def houseRobber(self, nums: List[int]) -> int:
        '''
        E.g. [1,2,3,1]
            n = 4
            max_value = 0
        '''
        n = len(nums)
        sums = [0] * n

        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])

        ## initial
        sums[0] = nums[0]
        sums[1] = np.maximum(nums[0], nums[1])

        ## computation
        for i in range(2, n):
            sums[i] = np.maximum(sums[i-2]+nums[i], sums[i-1])
        return sums[n-1]

        ## wrong answer
        # n = len(nums)
        # sum = nums[0]
        # max_value = 0
        # for i in range(1, n):
        #     sum += (nums[i]-nums[i-1])
        #     max_value = np.maximum(sum, max_value)
        # return max_value

if __name__ == '__main__':
    sol = Solution()
    ans = sol.houseRobber([1,2,3,1])
    print(ans)