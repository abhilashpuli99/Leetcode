# Last updated: 9/2/2025, 1:43:55 PM
class Solution:
    def jump(self, nums: List[int]) -> int:
        maxi=0
        count=0
        cj=0
        for i in range(len(nums)-1):
            maxi=max(maxi,i+nums[i])
            if i==cj:
                cj=maxi
                count+=1
        return count
