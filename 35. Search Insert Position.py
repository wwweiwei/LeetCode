from typing import List
class Solution():
    def searchInsertPosition(self, nums: List[int], target: int) -> int:
        '''
        Solution: binary search
        Time Complexity: O(logn)
        '''
        if nums == None:
            return 0
        left = 0
        right = len(nums) - 1
        middle = (left + right) // 2
        while left <= right:
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
            middle = (left + right) // 2

        return left
        # def binarySearch(left, right):
        #     middle = (left+right) // 2
        #     if nums[middle] == target:
        #         return middle
        #     elif middle == len(nums)-1:
        #         if nums[middle] > target:
        #             return middle
        #         else:
        #             return middle+1
        #     elif left == right and left == 0:
        #         return 0
        #     elif nums[middle] < target and target < nums[middle+1]:
        #         return middle + 1
        #     elif nums[middle] > target:
        #         return binarySearch(left, middle)
        #     else:
        #         return binarySearch(middle, right)

        # if nums == None:
        #     return 0
        # else:
        #     return binarySearch(0, len(nums))

if __name__ == "__main__":
    sol = Solution()
    ans = sol.searchInsertPosition(nums = [1], target = 0)
    print(ans)