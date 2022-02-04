from typing import List
class Solution:
    def reverseBits(self, n: int) -> int:
        str_n = bin(n)[2:]
        reverse_n = str_n[::-1]
        while len(reverse_n) != 32:
            reverse_n += '0'
        return int(reverse_n, 2)

if __name__ == '__main__':
    sol = Solution()
    ans = sol.reverseBits(0b00000010100101000001111010011100)
    print(ans)