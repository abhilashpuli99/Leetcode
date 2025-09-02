# Last updated: 9/2/2025, 1:42:31 PM
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]