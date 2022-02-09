from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strings = [str(digit) for digit in digits]
        a_string = ''. join(strings)
        ans = str(int(a_string) + 1)
        return [int(digit) for digit in ans]

if __name__ == '__main__':
    sol = Solution()
    ans = sol.plusOne([4,3,2,1])
    print(ans)