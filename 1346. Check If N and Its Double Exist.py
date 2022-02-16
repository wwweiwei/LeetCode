from typing import List
class Solution():
    def checkIfN(self, arr: List[int]) -> bool:
        '''
        E.g. 
            Input: arr = [10,2,5,3]
            Output: true
        '''
        arr.sort()
        print(arr)
        for i, v in enumerate(arr):
            if v % 2 == 0:
                if v > 0:
                    for j, num in enumerate(arr[:i]):
                        if i != j and v == num*2:
                            return True
                elif v <= 0:
                    for j, num in enumerate(arr):
                        if i != j and v == num*2:
                            return True
                        if num > 0:
                            break
        
        return False

if __name__ == "__main__":
    sol = Solution()
    ans = sol.checkIfN([10,2,5,3])
    print(ans)