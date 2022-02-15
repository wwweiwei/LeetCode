from typing import List
class Solution():
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ## sort by length
        strs.sort(key=len)

        min_word = strs[0]
        max = len(min_word)

        ## check if every word in the list have this prefix
        for _, word in enumerate(strs):
            for i in range(max):
                if word[i] != min_word[i]:
                    if max>i:
                        max = i
                if max == 0:
                    return ""

        if max == 0:
            return ""
        else:
            return min_word[:max]

if __name__ == "__main__":
    sol = Solution()
    ans = sol.longestCommonPrefix(["flower","flow","flight"])
    print(ans)