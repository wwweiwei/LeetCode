class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_list = list(s)
        s_list = s.split(' ')
        while s_list[-1] == '':
            s_list.pop()
        return len(s_list[-1])

if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLastWord("   fly me   to   the moon  "))