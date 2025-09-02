# Last updated: 9/2/2025, 1:43:05 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        result=[]
        finalres=0
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1] and nums[i] not in result:
                result.append(nums[i])
        for i in range(len(nums)):
            result.append(nums[i])
        for i in range(len(result)):
            finalres^=result[i]
        return finalres