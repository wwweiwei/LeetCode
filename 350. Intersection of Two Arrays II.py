import enum
from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        id1 = 0
        id2 = 0
        ans = []
        while id1!=len(nums1) and id2!=len(nums2):
            if nums1[id1] == nums2[id2]:
                ans.append(nums1[id1])
                id1 += 1
                id2 += 1
            elif nums1[id1] < nums2[id2]:
                id1 += 1
            elif nums1[id1] > nums2[id2]:
                id2 += 1
        return ans

if __name__ == '__main__':
    sol = Solution()
    ans = sol.intersection([4,9,5], [9,4,9,8,4])
    print(ans)