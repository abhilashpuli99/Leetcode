# Last updated: 9/2/2025, 1:43:31 PM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        subset=[]
        def dfs(start):
            result.append(subset[:])
            for i in range(start,len(nums)):
                subset.append(nums[i])
                dfs(i+1)
                subset.pop()
        dfs(0)
        return result
        