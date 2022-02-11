MAX = 2147483647
MIN = -2147483648

class Solution:
    def atoi(self, s: str) -> int:
        '''
        Implement the myAtoi(string s) function, 
        which converts a string to a 32-bit signed integer 
        (similar to C/C++'s atoi function).
        '''
        input = list(s.strip())
        ans = []

        if input == []:
            return 0
        elif input[0] == '-':
            isPositive = False
            input = input[1:]
        elif input[0] == '+':
            isPositive = True
            input = input[1:]
        else:
            isPositive = True

        for _, v in enumerate(input):
            if v in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                ans.append(v)
            else:
                break

        if ans == []:
            return 0
        else:
            if isPositive:
                return min(int(''.join(ans)), MAX)
            else:
                return max(-1 * int(''.join(ans)), MIN)

if __name__ == "__main__":
    sol = Solution()
    ans = sol.atoi("0032")
    print(ans)