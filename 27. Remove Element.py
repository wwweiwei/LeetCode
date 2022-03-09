class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        find = 0
        for i, v in enumerate(nums):
            if v == val:
                find += 1
            else:
                nums[i-find] = v
        return len(nums) - find