from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        sort -> conti. two same integers 
            -> yes -> return True
            -> no -> return False
        '''
        nums.sort()
        last = nums[0]
        for i, v in enumerate(nums):
            if last == v and i != 0:
                return True
            last = v
        return False
        
if __name__ == '__main__':
    sol = Solution()
    ans = sol.containsDuplicate([1,1,3,4,5])
    print(ans)