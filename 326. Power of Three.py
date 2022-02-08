class Solution:
    def powerOfThree(self, n: int) -> bool:
        '''
        Given an integer n, return true if it is a power of three. 
        Otherwise, return false
        '''
        if n == 0:
            return False
        n = float(n)
        while float.is_integer(n):
            if n == 1:
                return True
            else:
                n /= 3
                print('n: ', n)
        return False

if __name__ == '__main__':
    sol = Solution()
    ans = sol.powerOfThree(45)
    print(ans)