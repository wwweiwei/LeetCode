class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_count = {}
        for num in nums:
            if num not in num_count:
                num_count[num] = 1
            else:
                num_count[num] += 1
            if num_count[num] > len(nums)/2:
                return num