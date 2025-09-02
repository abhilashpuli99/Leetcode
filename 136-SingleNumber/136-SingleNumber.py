# Last updated: 9/2/2025, 1:43:07 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result=0
        for num in nums:
            result^=num
        return result
        