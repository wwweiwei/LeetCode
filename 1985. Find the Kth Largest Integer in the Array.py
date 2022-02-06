from typing import List
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        '''
        Problem: Return the string that represents the kth largest integer in nums.
        Method:
            Merge sort
            return kth largest
        Time complexity = O(nlogn)
        '''
        def mergeSort(arr):
            left = 0
            right = len(arr)
            if right == 1:  # just one element
                return arr
            middle = (left+right)//2
            arr1 = mergeSort(arr[:middle])
            arr2 = mergeSort(arr[middle:])
            arr = merge(arr1, arr2)
            return arr
        
        def merge(arr1, arr2):
            arr = []
            i, j = 0, 0
            while i != len(arr1) or j != len(arr2):                
                if i == len(arr1) and j != len(arr2):
                    arr.append(arr2[j])
                    j += 1
                elif j == len(arr2) and i != len(arr1):
                    arr.append(arr1[i])
                    i += 1
                elif int(arr1[i]) > int(arr2[j]):
                    arr.append(arr2[j])
                    j += 1
                else:
                    arr.append(arr1[i])
                    i += 1
            return arr

        return mergeSort(nums)[len(nums)-k]

if __name__ == '__main__':
    sol = Solution()
    ans = sol.kthLargestNumber(nums = ["3","6","7","10"], k = 4)
    print(ans)