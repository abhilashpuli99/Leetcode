# Last updated: 9/2/2025, 1:44:02 PM
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(0,len(nums)):
            if nums[i]>=target:
                return i
        return len(nums)