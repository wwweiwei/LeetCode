class Solution:
    def calPoints(self, ops: List[str]) -> int:
        ans = []
        
        while ops:
            op = ops.pop(0)
            if op == 'C':
                ans.pop() ## pop the last element
            elif op == 'D':
                ans.append(ans[-1]*2)
            elif op == '+':
                ans.append(ans[-1]+ans[-2])
            else:
                ans.append(int(op))
        
        return sum(ans)
