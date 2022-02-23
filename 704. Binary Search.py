from typing import List
class Solution:
    def binarySearch(self, nums: List[int], target: int) -> int:
        '''
        Given an array of integers nums which is sorted in ascending order, 
        and an integer target, write a function to search target in nums. 
        If target exists, then return its index. Otherwise, return -1.
        
        You must write an algorithm with O(log n) runtime complexity.
        
        Input: nums = [-1,0,3,5,9,12], target = 9
        Output: 4
        '''
        ## edge case
        if nums is None:
            return -1

        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1

        return -1

if __name__ == "__main__":
    sol = Solution()
    ans = sol.binarySearch(nums = [-1,0,3,5,9,12], target = 9)
    print(ans)