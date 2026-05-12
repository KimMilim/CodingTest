from collections import *

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        words = defaultdict(list)
        for s in strs:
            tmp = []
            for c in s:
                tmp.append(c)
            tmp.sort()
            words["".join(tmp)].append(s)

        answer = []
        for key, value in words.items():
            answer.append(value)
        
        return answer


            


        

        