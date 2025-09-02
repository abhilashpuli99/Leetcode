# Last updated: 9/2/2025, 1:42:28 PM
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen={}
        for i,val in enumerate(nums):
                if val in seen and i-seen[val]<=k:
                    return True
                else:
                    seen[val]=i
        return False