class Solution:
    def firstNonRepeatChar(self, s: str) -> int:
        freq = {}
        for i, value in enumerate(s):
            if s[i] in freq:
                freq[value] += 1
            else:
                freq[value] = 1
        for k, v in freq.items():
            if v == 1:
                for i, value in enumerate(s):
                    if value == k:
                        return i
        return -1

if __name__ == '__main__':
    sol = Solution()
    ans = sol.firstNonRepeatChar('aabc')
    print(ans)

            
            