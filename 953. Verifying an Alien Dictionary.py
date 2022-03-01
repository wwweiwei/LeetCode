import numpy as np
from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        '''
        dict:
            key = char, value = order
            e.g. {(char, order), ..}
        '''
        order_dict = {}
        for i in range(len(order)):
            order_dict[order[i]] = i
        
        if words is None:
            return True
        prev = words[0]

        for i, word in enumerate(words):
            if i != 0:
                for j in range(np.maximum(len(prev), len(word))):
                    if j >= len(word):
                        return False
                    elif j >= len(prev):
                        prev = word
                        break
                    elif order_dict[prev[j]] > order_dict[word[j]]:
                        return False
                    elif order_dict[prev[j]] < order_dict[word[j]]:
                        prev = word
                        break

                prev = word
                if i == len(words)-1:
                    return True

if __name__ == "__main__":
    sol = Solution()
    ans = sol.isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz")
    print(ans)