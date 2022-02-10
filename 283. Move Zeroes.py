from typing import List
import collections
class Solution:
    def moveZeros(self, nums: List[int]) -> List[int]:
        '''
        Input: nums = [0,1,0,3,12]
        Output: [1,3,12,0,0]
        '''
        nonzero_index = 0
        length = len(nums)
        for i in range(length):
            if nums[i] != 0:
                nums[nonzero_index] = nums[i]
                nonzero_index += 1
        while nonzero_index < length:
            nums[nonzero_index] = 0
            nonzero_index += 1

        return nums

if __name__ == "__main__":
    sol = Solution()
    ans = sol.moveZeros(nums = [0,1,0,3,12])
    print(ans)