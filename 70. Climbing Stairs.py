import numpy as np
arr = np.zeros(10)

class Solution:
    def dp(self, n: int) -> int:
        '''
        either 1 or 2 steps every time
        how many ways?
        Solution: 
            dp(n) = dp(n-1) + dp(n-2)
        '''
        ## buttom up
        for i in range(3, n+1):
            arr[i] = arr[i-1] + arr[i-2]
        return int(arr[n])

        ## top down
        # if arr[n] != 0:
        #     return int(arr[n])
        # else:
        #     arr[n] = self.dp(n-1)+self.dp(n-2)
        #     return int(arr[n])

        ## TLE
        # if n==1:
        #     return 1
        # elif n==2:
        #     return 2
        # else:
        #     return self.dp(n-2)+self.dp(n-1)

if __name__ == '__main__':
    sol = Solution()
    arr[1] = 1
    arr[2] = 2
    ans = sol.dp(3)
    print(ans)   