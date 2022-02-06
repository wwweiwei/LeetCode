import random
from typing import List
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums
    
    def shuffle(self) -> List[int]:
        tmp = self.nums.copy()
        random.shuffle(tmp)
        return tmp

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

if __name__ == '__main__':
    sol = Solution([1, 2, 3])
    param_1 = sol.reset()
    param_2 = sol.shuffle()