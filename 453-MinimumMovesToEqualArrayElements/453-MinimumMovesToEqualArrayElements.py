# Last updated: 9/2/2025, 1:41:52 PM
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums)-min(nums)*len(nums)