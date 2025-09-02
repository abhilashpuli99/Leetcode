# Last updated: 9/2/2025, 1:43:25 PM
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result=[]
        subset=[]
        nums.sort()
        def dfs(start):
            result.append(subset[:])
            for i in range(start,len(nums)):
                if i!=start and nums[i]==nums[i-1]:
                    continue
                subset.append(nums[i])
                dfs(i+1)
                subset.pop()
        dfs(0)
        return result