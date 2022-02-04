from queue import Empty


class Solution:
    def isValid(self, s: str) -> bool:
        '''
        E.g.
            Input: s = "()[]{}"
            Output: true
        '''
        stack = []
        for i in range(len(s)):
            if s[i] == ')':
                if stack == []:
                    return False
                if stack.pop() != '(':
                    return False
            elif s[i] == ']':
                if stack == []:
                    return False
                if stack.pop() != '[':
                    return False
            elif s[i] == '}':
                if stack == []:
                    return False
                if stack.pop() != '{':
                    return False
            else:
                stack.append(s[i])
        if stack == []:
            return True
        else:
            return False
        
if __name__ == '__main__':
    sol = Solution()
    ans = sol.isValid("()[]")
    print(ans)