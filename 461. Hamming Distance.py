class Solution():
    def hammingDistance(self, x: int, y: int) -> int:
        bitwise_or = x ^ y
        str_ = str(bin(bitwise_or))[2:]
        count = 0
        for i in range(0, len(str_)):
            if str_[i] == '1':
                count += 1
        return count

if __name__ == '__main__':
    sol = Solution()
    ans = sol.hammingDistance(3, 1)
    print(ans)