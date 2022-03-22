class Solution:
    def mySqrt(self, x: int) -> int:
        if x >= 1:
            cur = 1
            while True:
                if cur * cur <= x and x < (cur+1) * (cur+1):
                    return cur
                cur += 1
        else:
            return 0
        