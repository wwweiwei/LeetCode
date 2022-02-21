from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ## edge case
        if nums is None or len(nums) < 3:
            return None

        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i-1]:
                continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v, -v-x, x))
        return list(res)
        
if __name__ == "__main__":
    sol = Solution()
    ans = sol.threeSum(nums = [-1,0,1,2,-1,-4])
    print(ans)