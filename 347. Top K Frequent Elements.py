class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for value in nums:
            if value in freq:
                freq[value] += 1
            else:
                freq[value] = 1
        
        freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        
        ans = []
        for i, key in enumerate(freq.keys()):
            if i < k:
                ans.append(key)
        
        return ans
