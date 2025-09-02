# Last updated: 9/2/2025, 1:42:16 PM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res=[]
        zero=0
        for i in range(len(nums)):
            if nums[i]==0:
                zero+=1
            else:
                res.append(nums[i])
        res.extend([0]*zero)
        nums[:]=res