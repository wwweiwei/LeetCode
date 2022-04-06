from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def merge(left, right):
            ans = []
            while left and right:
                concat1 = str(left[0])+str(right[0])
                concat2 = str(right[0])+str(left[0])
                if int(concat1) > int(concat2):
                    ans.append(left[0])
                    left.pop(0)
                else:
                    ans.append(right[0])
                    right.pop(0)
            if len(left):
                ans+=left
            else:
                ans+=right
            return ans
        
        def sort(nums):
            if len(nums) < 2:
                return nums
            
            middle = len(nums) // 2
            
            return merge(sort(nums[:middle]), sort(nums[middle:]))
        
        sort_list = sort(nums)
        ans = ''
        for digit in sort_list:
            ans += str(digit)
            
        if int(ans) == 0:
            return str(0)
        else:
            return ans

#         ans = ''
#         digits = []
#         for num in nums:
#             if num != '':
#                 for digit in list(str(num)):
#                     digits.append(digit)
        
#         digits.sort(reverse=True)
#         for digit in digits:
#             ans += str(digit)
            
#         return ans

if __name__ == '__main__':
    sol = Solution()
    ans = sol.largestNumber(nums = [3,30,34,5,9])
    print(ans)