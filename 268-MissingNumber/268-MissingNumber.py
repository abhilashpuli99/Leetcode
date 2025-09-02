# Last updated: 9/2/2025, 1:42:19 PM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        summ=0
        for i in range(n+1):
            summ+=i
        if 0 not in nums:
            return 0
        else:
            return summ-sum(nums)