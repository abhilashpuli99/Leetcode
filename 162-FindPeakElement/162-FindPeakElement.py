# Last updated: 9/2/2025, 1:42:53 PM
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """num=max(nums)
        idx=nums.index(max(nums))
        return idx"""
        left,right=0,len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]>nums[mid+1]:
                right=mid
            else:
                left=mid+1     
        return left

        