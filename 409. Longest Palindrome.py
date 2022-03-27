class Solution:
    def longestPalindrome(self, s: str) -> int:
            if s == '':
                return 0
            
            dict_letter = {}
            list_s = list(s)
            for _, value in enumerate(list_s):
                if value in dict_letter:
                    dict_letter[value] += 1
                else:
                    dict_letter[value] = 1
            
            length = 0
            single_letter = False
            for key, value in dict_letter.items():
                if (value % 2) == 0:
                    length += value
                else:
                    single_letter = True
                    length += (value - 1)
                    
            if single_letter == True:
                length += 1
                
            return int(length)
            
#             list_s = list(s)
#             max_len = 1
#             for i in range(len(list_s)):
#                 left = i
#                 right = left+1
#                 cur = 0
#                 while (left>=0 and right < len(list_s) and list_s[left] == list_s[right]):
#                     cur += 2
#                     left -= 1
#                     right += 1