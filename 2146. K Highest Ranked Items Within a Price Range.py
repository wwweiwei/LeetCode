import numpy as np
from typing import List

class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        # ans = []
        # dist = {} ## {(row, col), distance}

        # for rid, row in enumerate(grid):
        #     for cid, value in enumerate(row):
        #         if value <= pricing[1] and value >= pricing[0]:
        #             distance = np.abs(rid-start[0]) + np.abs(cid-start[1])
        #             dist[(rid, cid, value)] = distance
        
        # ## sorted by value
        # sort_dict = dict(sorted(dist.items(), key=lambda item: (item[1], item[0][2], item[0][0], item[0][1])))
        # print('sort_dict: ', sort_dict)

        # for key in sort_dict.keys():
        #     ans.append([key[0], key[1]])
        #     if len(ans) == k:
        #         return ans
        # return ans

        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        hp = []
        q = deque([start+[0]])
        while q:
            i,j,d = q.popleft()
            if grid[i][j] == 0:
                continue
            if pricing[0] <= grid[i][j] <= pricing[1]:
                heappush(hp,(-d,-grid[i][j],-i,-j))
                if len(hp) > k:
                    heappop(hp)
            grid[i][j] = 0
            for x,y in dirs:
                if 0 <= i+x < len(grid) and 0 <= j+y < len(grid[0]):
                    q.append([i+x,j+y,d+1])
        res = []
        while hp:
            _,_,a,b = heappop(hp)
            res.append([-a,-b])
        return res[::-1]

if __name__ == '__main__':
    sol = Solution()
    ans = sol.highestRankedKItems(grid = [[1,1,1],[0,0,1],[2,3,4]], pricing = [2,3], start = [0,0], k = 3)
    print(ans)
