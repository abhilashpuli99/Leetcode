# Last updated: 9/2/2025, 1:42:30 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq=set()
        for i in range(len(nums)):
            if nums[i] in freq:
                return True
            else:
                freq.add(nums[i])
        return False
