class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(999999):
            if i*i == num:
                return True
            elif i*i > num:
                return False
            
        return False