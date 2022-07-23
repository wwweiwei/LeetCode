class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        nums.append(float('inf'))
        res, start = [], 0
        
        for i in range(len(nums)-1):
            if nums[i + 1] != nums[i] + 1:
                if i == start:
                    res.append(str(nums[i]))
                else:
                    res.append("%s->%s" % (nums[start], nums[i]))
                start = i + 1
                               
        return res