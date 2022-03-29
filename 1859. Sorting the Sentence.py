class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        dict_word = {}
        ans = ''
        
        for i, word in enumerate(words):
            order = int(word[-1])
            dict_word[order] = word[0:-1]

        print('dict_word: ', dict_word)
            
        for i in range(1, len(words)+1):
            ans += dict_word[i]
            if i != len(words):
                ans += ' '
            
        return ans

if __name__ == '__main__':
    sol = Solution()
    ans = sol.sortSentence(s = "is2 sentence4 This1 a3")
    print(ans)