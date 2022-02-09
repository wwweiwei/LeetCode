from typing import List
class Solution:
    def romanToInteger(self, s: str) -> int:
        '''
        Symbol       Value
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
        '''
        roman = list(s)[::-1]
        total = 0
        label = 'I'
        for i, v in enumerate(roman):
            if v == 'I':
                if label == 'I':
                    total += 1
                else:
                    total -= 1
            elif v == 'V':
                if label in ['I', 'V']:
                    total += 5
                    label = 'V'
                else:
                    total -= 5
            elif v == 'X':
                if label in ['I', 'V', 'X']:
                    total += 10
                    label = 'X'
                else:
                    total -= 10
            elif v == 'L':
                if label in ['I', 'V', 'X', 'L']:
                    total += 50
                    label = 'L'
                else:
                    total -= 50
            elif v == 'C':
                if label in ['I', 'V', 'X', 'L', 'C']:
                    total += 100
                    label = 'C'
                else:
                    total -= 100
            elif v == 'D':
                if label in ['I', 'V', 'X', 'L', 'C', 'D']:
                    total += 500
                    label = 'D'
                else:
                    total -= 500 
            elif v == 'M':
                if label in ['I', 'V', 'X', 'L', 'C', 'D', 'M']:
                    total += 1000
                    label = 'M'
                else:
                    total -= 1000

        return total

if __name__ == '__main__':
    sol =Solution()
    ans = sol.romanToInteger("MCMXCIV")
    print(ans)