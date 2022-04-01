class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        index = 0
        
        while coins>0 and index<len(costs):
            if costs[index] <= coins:
                coins -= costs[index]
                index += 1
            else:
                return index
            
        return index