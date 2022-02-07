import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        primes = [True] * n
        primes[0], primes[1] = False, False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                # faster
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
                ## primes[i * 2: n: i] = [False] * len(primes[i * 2: n: i])
        return sum(primes)

        ## TLE
        # count = 0
        # for i in range(2, n):
        #     if i == 2 or i == 3:
        #         count += 1
        #     for j in range(2, int(math.sqrt(i))+1):
        #         if i % j == 0:
        #             break
        #         elif j == int(math.sqrt(i)):
        #             count += 1
        # return count

if __name__ == '__main__':
    sol = Solution()
    ans = sol.countPrimes(10)
    print(ans)