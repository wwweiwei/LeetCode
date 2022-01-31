from typing import List
class Solution:
    def removeDuplicate(self, nums: List[int]) -> int:
        '''
        Given an integer array nums sorted in non-decreasing order, 
        remove the duplicates in-place such that each unique element appears only once. 
        The relative order of the elements should be kept the same.
        '''
        i = 0 # count of not duplicate
        j = 1 # cur
        while j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i+1
        # count = 0
        # last = -101
        # for i, v in enumerate(nums):
        #     if last == v:
        #         count+=1
        #     last = v
        # count = len(nums) - count
        # nums = list(set(nums))
        # return count

if __name__ == '__main__':
    sol = Solution()
    ans = sol.removeDuplicate([1,1,3,4,5])
    print(ans)