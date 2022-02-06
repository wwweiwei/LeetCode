from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ## replace nums1 by nums2
        for i in range(m,m+n):
            nums1[i] = nums2[i-m]

        ## implement merge sort
        def mergeSort(arr):
            if len(arr) == 1:
                return arr
            left = 0
            right = len(arr)
            middle = (left+right) // 2 ## floor
            arr1 = mergeSort(arr[left:middle])
            arr2 = mergeSort(arr[middle:right])
            arr = merge(arr1, arr2)
            return arr
        
        def merge(arr1, arr2):
            arr = []
            i, j = 0, 0
            while i != len(arr1) or j != len(arr2):
                if i == len(arr1):
                    arr.append(arr2[j])
                    j += 1
                elif j == len(arr2):
                    arr.append(arr1[i])
                    i += 1                
                elif arr1[i] < arr2[j]:
                    arr.append(arr1[i])
                    i += 1
                else:
                    arr.append(arr2[j])
                    j += 1
            return arr

        nums1 = mergeSort(nums1)
        for i in range(m+n):
            nums1[i] = ans[i]

        return nums1

if __name__ == '__main__':
    sol = Solution()
    ans = sol.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
    print(ans)