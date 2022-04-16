class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if stones is None:
            return 0
        
        while len(stones)>1:
            stones.sort()
            if stones[-1] == stones[-2]:
                stones.pop()
                stones.pop()
            else:
                stones[-1] = stones[-1] - stones[-2]
                stones.pop(-2)
                
            if stones is None:
                return 0
         
        if stones:  
            return stones[0]
        else:
            return 0