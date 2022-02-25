# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 0
        high = n
        while True:
            middle = (low + high) // 2
            ans = guess(middle)
            if ans == 0:
                return middle
            elif ans == -1:
                high = middle - 1
            else:
                low = middle + 1