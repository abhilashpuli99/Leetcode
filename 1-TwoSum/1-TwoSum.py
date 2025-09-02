# Last updated: 9/2/2025, 1:44:30 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,val in enumerate(nums):
            difference=target-val
            if difference in seen:
                return [seen[difference],i]
            seen[val]=i
        