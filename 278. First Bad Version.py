from typing import List
class Solution:
    def firstBadVersion(self, n: int) -> int:
        ## Binary Search
        def isBadVersion(i: int) -> bool:
            if i >= 4:
                return True
            else:
                return False

        left = 1
        right = n
        while True:
            middle = (left+right) // 2
            if isBadVersion(middle) == True and isBadVersion(middle-1) == False:
                return middle
            elif isBadVersion(middle) == True:
                right = middle-1
            else:
                left = middle+1

        ## TLE
        # def binary_search(lst) -> int:
        #     middle = len(lst) // 2
        #     if len(lst) == 1:
        #         if isBadVersion(lst[middle]) == True:
        #             return lst[0]
        #         else:
        #             return lst[0] + 1
        #     else:
        #         if isBadVersion(lst[middle]) == True:
        #             ans = binary_search(lst[0:middle])
        #         else:
        #             ans = binary_search(lst[middle:len(lst)])
        #     return ans

        # input = [i for i in range(1, n+1)]
        # return binary_search(input)

    
if __name__ == '__main__':
    sol = Solution()
    ans = sol.firstBadVersion(5)
    print(ans)   