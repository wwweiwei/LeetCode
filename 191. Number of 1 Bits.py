class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1") 

        # ## runtime error
        # str_n = str(n)
        # sum = 0
        # for i in range(32):
        #     sum += int(str_n[i])
        # return sum

if __name__ == '__main__':
    sol = Solution()
    ans = sol.hammingWeight(19)
    print(ans)