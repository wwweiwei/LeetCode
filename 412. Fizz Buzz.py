from array import array
import numpy as np

class Solution:
    def fizzBuzz(self, n: int) -> array:
        answer = []
        for i in range(n):
            cur = i+1
            if cur%3 == 0 and cur%5 == 0:
                answer.append("FizzBuzz")
            elif cur%3 == 0:
                answer.append("Fizz")
            elif cur%5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(cur))
        return answer
if __name__ == "__main__":
    sol = Solution()
    answer = sol.fizzBuzz(6)
    print(answer)