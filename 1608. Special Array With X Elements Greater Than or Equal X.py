from typing import List

def specialArray(nums: List[int]) -> int:
    '''
    You are given an array nums of non-negative integers. 
    nums is considered special if there exists a number x 
    such that there are exactly x numbers in nums that are greater than or equal to x.
    E.g. 
        Input: nums = [3,5]
        Output: 2
    '''
    nums.sort(reverse = True)
    print(nums)
    for i in range(len(nums)+1): ## E.g. 0, 1, 2
        for j in range(len(nums)):
            if i <= nums[j]: ## greater than or equal to x
                if len(nums) == i and j == len(nums)-1: ## i equal to length
                    return i
                elif j >= i: ## too much
                    break
            else:
                if j == i: ## exact i
                    return i
                break
    return -1


ans = specialArray(nums = [3,6,7,7,0])
print(ans)