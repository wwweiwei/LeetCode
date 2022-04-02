class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, index, two = 0, 0, len(nums) - 1
        while index <= two:
            if nums[index] == 0:
                nums[zero], nums[index] = nums[index], nums[zero]
                zero += 1
                index += 1
            elif nums[index] == 2:
                nums[index], nums[two] = nums[two], nums[index]
                two -= 1
            else:
                index += 1
        ## wrong
        # for i in range(len(nums)-1):
        #     for j in range(i, len(nums)-1):
        #         if nums[j] > nums[j+1]:
        #             tmp = nums[j]
        #             nums[j] = nums[j+1]
        #             nums[j+1] = tmp
        