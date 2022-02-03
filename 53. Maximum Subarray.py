from typing import List
import numpy as np
class Solution:
    def maxSubarray(self, nums: List[int]) -> int:
        ## initial
        n = len(nums)
        sum = nums[0]
        max_value = nums[0]

        ## computation
        for i in range(1, n):
            sum = np.maximum(sum+nums[i], nums[i])
            max_value = np.maximum(sum, max_value)
    
        return max_value

        # wrong answer
        # ## initial
        # n = len(nums)
        # arr = [0] * n
        # conti_arr = [0] * n

        # def getContiArray(n):
        #     if nums[n]>0:
        #         conti_arr[n] = conti_arr[n-1] + nums[n]
        #         return conti_arr[n]
        #     else:
        #         conti_arr[n-1]

        # arr[0] = 0
        # arr[1] = nums[0]
        # conti_arr[0] = nums[0]

        # for i in range(2, n):
        #     arr[i] = np.maximum(arr[i-1], getContiArray(i-1))

        # print('arr: ', arr)
        # print('conti_arr: ', conti_arr)

        # return np.maximum(arr[n-1], conti_arr[n-1])

if __name__ == '__main__':
    sol = Solution()
    ans = sol.maxSubarray([-2,1,-3,4,-1,2,1,-5,4])
    print(ans)