class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        power = -31
        last = -1
        while power <= 31 and last < n:
            cur = 2**power
            if cur == n:
                return True
            last = cur
            power += 1
        return False