import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        Given a string s, 
        return true if it is a palindrome, or false otherwise.
        E.g. s = "A man, a plan, a canal: Panama" => True
        '''
        if s.strip() == '':
            return True
        ## delete space and non-alphanumeric characters, change into lower char
        s = s.strip().lower()
        s = re.sub(r'[\W]', '', s)
        s = re.sub('_', '', s)
        print('s: ', s)
        ## check whether is palindrome
        if s == s[::-1]:
            return True
        else:
            return False

if __name__ == '__main__':
    sol = Solution()
    ans = sol.isPalindrome('A man, a plan, a canal: Panama')
    print(ans)