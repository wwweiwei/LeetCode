from xmlrpc.client import boolean

class Solution:
    def isAnagram(self, s: str, t: str) -> boolean:
        '''
        Given two strings s and t, 
        return true if t is an anagram of s, and false otherwise.
        E.g. s = 'anagram', t = 'nagaram' => return True
        '''
        s_dict = {}
        t_dict = {}
        for i, char in enumerate(s):
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1
        for i, char in enumerate(t):
            if char in t_dict:
                t_dict[char] += 1
            else:
                t_dict[char] = 1
        if s_dict == t_dict:
            return True
        else:
            return False     


if __name__ == '__main__':
    sol = Solution()
    ans = sol.isAnagram('anagram', 'nagaram')
    print(ans)
