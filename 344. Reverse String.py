from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(int(len(s)/2)):
            temp = s[i]
            s[i] = s[len(s)-1-i]
            s[len(s)-1-i] = temp
        ## not in place
        # s = s[::-1]

if __name__ == '__main__':
    solution = Solution()
    input = ['H', 'e', 'l', 'l', 'o']
    solution.reverseString(input)