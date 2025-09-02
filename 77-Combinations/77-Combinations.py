# Last updated: 9/2/2025, 1:43:33 PM
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        comb=[]
        result=[]
        def dfs(start):
            if len(comb)==k:
                result.append(comb[:])
            for i in range(start,n+1):
                comb.append(i)
                dfs(i+1)
                comb.pop()
        dfs(1)
        return result