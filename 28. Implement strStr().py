class Solution():
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        elif needle not in haystack:
            return -1
            
        if len(haystack) < len(needle):
            return -1

        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if haystack[i:i+len(needle)] == needle[0:]:
                    return i

        return -1

if __name__ == "__main__":
    sol = Solution()
    ans = sol.strStr(haystack = "hello", needle = "ll")
    print(ans)
