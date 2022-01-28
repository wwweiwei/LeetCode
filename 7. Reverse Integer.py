class Solution():
    def reverseInteger(self, x: int) -> int:
        negative = False
        if x == 0:
            return 0
        elif x < 0:
            ans = str(-x)[::-1]
            negative = True
        else:
            ans = str(x)[::-1]
        while ans[0] == 0: # eliminate zero
            ans = ans[1:]
        
        if int(ans) < -(2**31) or int(ans) > ((2**31) - 1): # out of boundary
            return 0
        elif negative == True:
            return -1 * int(ans)
        else:
            return int(ans)

if __name__ == '__main__':
    sol = Solution()
    ans = sol.reverseInteger(1534236469)
    print(ans)