from typing import List
class Solution:
    def lengthofLIS(self, nums: List[int]) -> int:
        '''
        f(n)
            w/ n -> f(n-1)+1
            w/o n -> f(n-1)
        '''        
        tmp = []
        for n in nums:
            left = 0
            right = len(tmp)-1

            while left <= right: # binary search
                middle = left + (right - left) // 2
                if n <= tmp[middle]: 
                    right = middle - 1
                else: 
                    left = middle + 1

            if left == len(tmp):
                tmp.append(n)
            else:
                tmp[left] = n

        return len(tmp)      

        ## not dp solution
        # tmp = [1] * len(nums)
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             tmp[i] = max(tmp[i], tmp[j]+1)
        # return max(tmp)

if __name__ == '__main__':
    sol = Solution()
    ans = sol.lengthofLIS([0,1,0,3,2,3])
    print(ans)