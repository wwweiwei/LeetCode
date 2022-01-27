class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## O(n)
        num_dict = {}
        for idx, value in enumerate(nums):
            remain = target - nums[idx]
            if remain in num_dict:
                return [idx, num_dict[remain]]
            num_dict[value] = idx
        ## O(n^2)    
        # for idx, value in enumerate(nums):
        #     value = nums[idx]
        #     for idx2, value2 in enumerate(nums):
        #         if idx!=idx2 and nums[idx] + nums[idx2] == target:
        #             return [idx, idx2]