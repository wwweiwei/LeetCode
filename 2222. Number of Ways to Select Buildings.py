class Solution:
    def numberOfWays(self, s: str) -> int:
	'''
	time: O(n)
	space: O(1)
	'''
        count = 0 
        record = [[0]*2 for _ in range(2)]
        
        for i in range(len(s)):
            current = int(s[i])
            count += record[1][1-current]

            record[1][current] += record[0][1-current]
            record[0][current] += 1            
        return count

if __name__ == '__main__':
    sol = Solution()
    ans = sol.numberOfWays(s = "001101")
    print(ans)