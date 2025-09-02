# Last updated: 9/2/2025, 1:43:51 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=dict()
        for word in strs:
            sword=''.join(sorted(word))
            if sword not in result:
                result[sword]=[]
            result[sword].append(word)
        return list(result.values())
        
        