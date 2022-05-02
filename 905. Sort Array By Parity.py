class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd_id = 0
        for cur_id, num in enumerate(nums):
            if num % 2 == 0: # even
                tmp = nums[odd_id]
                nums[odd_id] = num
                nums[cur_id] = tmp
                odd_id += 1
        return nums
    
        # ans = []
        # for num in nums:
        #     if num%2 == 1: # odd
        #         ans.append(num)
        #     else: # even
        #         ans.insert(0, num)
        # return ans