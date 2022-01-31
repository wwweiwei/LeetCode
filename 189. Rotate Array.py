from typing import List
class Solution:
    def rotateArray(self, nums: List[int], k: int) -> None:
        '''
        E.g. 
            input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
            [7, 1, 2, 3, 4, 5, 6]
            ...
            output: [5, 6, 7, 1, 2, 3, 4]
        Method: 
        '''
        length = len(nums)
        k = k % length
        for i  in range(length):
            if length == k:
                pass
            elif i < length - k: # 4
                nums.append(nums[0])
                del nums[0]
        print(nums)

if __name__ == '__main__':
    sol = Solution()
    sol.rotateArray([1, 2, 3, 4, 5, 6, 7], 3)