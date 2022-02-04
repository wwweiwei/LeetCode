from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        E.g.
            Input: nums = [3,0,1]
            Output: 2
        '''
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)

        ## Better solution
        # op1 = int ((n * (n+1)) / 2)
        # return op1 - sum(nums)

if __name__ == '__main__':
    sol = Solution()
    ans = sol.missingNumber([0, 1])
    print(ans)