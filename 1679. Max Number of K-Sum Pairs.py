class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ## TLE
        # count = 0
        # for i, num in enumerate(nums):
        #     if num != 0:
        #         left = k - num
        #         if left > 0:
        #             for j, test in enumerate(nums):
        #                 if i != j and left == test:
        #                     nums[i] = 0
        #                     nums[j] = 0
        #                     count += 1
        #                     break
        # return count
        
        ct = Counter(nums)
        res = 0
        for n in ct:
            left = k - n
            if n == left:
                res += ct[n] // 2
                continue    
            if n < left:
                res += min(ct[n], ct[left])
        return res