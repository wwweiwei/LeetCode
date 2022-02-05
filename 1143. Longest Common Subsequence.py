class Solution:
    def LCS(self, text1: str, text2: str) -> int:
        '''
        the last is the same: f(text1[m-1], text2[n-1]) +1
        the last is not the same: max( f(text1[m-1], text2[n]), f(text1[m], text2[n-1]))
        '''
        tmp = [[0] * (len(text2)+1) for i in range(len(text1)+1)]

        for n in range(1, len(text1)+1, 1):
            for m in range(1, len(text2)+1, 1):
                if text1[n-1] == text2[m-1]:
                    tmp[n][m] = tmp[n-1][m-1] + 1
                else:
                    tmp[n][m] = max(tmp[n][m-1], tmp[n-1][m])

        return tmp[len(text1)][len(text2)]

        ## TLE
        # def dp(n, m):
        #     if n<0 or m<0:
        #         return 0
        #     if text1[n] == text2[m]:
        #         return dp(n-1, m-1) + 1
        #     else:
        #         return max( dp(n-1, m), dp(n, m-1))
        
        # return dp(len(text1)-1, len(text2)-1)

if __name__ == '__main__':
    sol = Solution()
    ans = sol.LCS("abcba", "abcbcba")
    print(ans)