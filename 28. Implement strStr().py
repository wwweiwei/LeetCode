class Solution():
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        elif needle not in haystack:
            return -1
            
        list_h = list(haystack)
        list_n = list(needle)
        if len(list_h) < len(list_n):
            return -1

        for i in range(len(list_h)):
            id = i
            for j, n in enumerate(list_n):
                if list_h[id] != n:
                    break
                elif j == len(list_n)-1:
                    return id -(len(list_n)-1)
                id += 1
                if id == len(list_h):
                    return -1
        return -1

if __name__ == "__main__":
    sol = Solution()
    ans = sol.strStr(haystack = "hello", needle = "ll")
    print(ans)
