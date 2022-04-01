import numpy as np
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []
        num_i = np.minimum(len(l), len(r))
        
        for i in range(num_i):
            if l[i] < len(nums):
                end = np.minimum(r[i], len(nums)-1)
                check_list = nums[l[i]:end+1]
                if len(check_list) == 1:
                    answer.append(True)
                else:
                    check_list.sort()
                    tmp = check_list[0]
                    minus = check_list[1] - check_list[0]
                    for i in range(1, len(check_list)):
                        if check_list[i] - tmp == minus:
                            tmp = check_list[i]
                            if i == len(check_list)-1:
                                answer.append(True)
                        else:
                            answer.append(False)
                            break
            else:
                answer.append(False)
                
        return answer
        