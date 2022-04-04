from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        dict = { sort_order : original_order , ...}
        '''
        ## if the key doesn't exist, it will not error
        dic = defaultdict(list) 
        
        for s in strs:
            dic[''.join(sorted(s))].append(s)
        
        return dic.values()