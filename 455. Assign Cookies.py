class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        count = 0
        for _, child in enumerate(g):
            if i == len(s):
                return count
            for j in range(i, len(s)):
                if s[j] >= child:
                    count += 1
                    i = j+1
                    break
        return count