class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        for i in range(rowIndex):
            for j in range(i, 0, -1):
                ans[j] += ans[j-1]
            ans.append(1)
        return ans

if __name__ == "__main__":
    sol = Solution()
    ans = sol.getRow(rowIndex = 3)
    print(ans)