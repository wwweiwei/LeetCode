class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        list_s = []
        list_t = []
        
        for i in s:
            if i == '#':
                if list_s:
                    list_s.pop()
            else:
                list_s.append(i)

        for i in t:
            if i == '#':
                if list_t:
                    list_t.pop()
            else:
                list_t.append(i)
                
        return list_s == list_t