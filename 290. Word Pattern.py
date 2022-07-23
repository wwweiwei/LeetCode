class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list_s = s.split(' ')
        if len(pattern) != len(list_s):
            return False
        return len(set(pattern)) == len(set(list_s)) == len(set(zip(pattern, list_s)))