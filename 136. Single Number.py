from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        create a dictionary -> check if the value is in the dictionary
        '''
        number_freq = {}
        for _, v in enumerate(nums):
            if v in number_freq:
                del number_freq[v]
            else:
                number_freq[v] = 1
        for key in number_freq:
            return key

if __name__ == '__main__':
    sol = Solution()
    ans = sol.singleNumber([1,1,2,3,2])
    print(ans)
            