class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ans = []
        for i, v in enumerate(nums):
            if v == target:
                ans.append(i)
            elif v > target:
                break
        return ans
        