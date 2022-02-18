'''
You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

Input: mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
Output: [2,0,3]
'''
from typing import List
import numpy as np

def kWeak(mat: List[List[int]], k: int) -> List[int]:
    ans = {}
    for row_id, row_value in enumerate(mat):
        ans[row_id] = row_value.count(1)
        
    ans = sorted(ans, key = ans.get)
    
    return ans[:k]

#     num_one = []
#     for row_id, row_value in enumerate(mat):
#         num_one.append(row_value.count(1))
        
#     ans = []
    
#     for i in range(k):
#         min_ = np.inf
#         index = 0
#         for id, value in enumerate(num_one):
#             if value < min_:
#                 min_ = value
#                 index = id
#         ans.append(index)
#         num_one[index] = np.inf
        
#     return ans

ans = kWeak(mat = 
        [[1,1,0,0,0],
         [1,1,1,1,0],
         [1,0,0,0,0],
         [1,1,0,0,0],
         [1,1,1,1,1]], k = 3)
print(ans)