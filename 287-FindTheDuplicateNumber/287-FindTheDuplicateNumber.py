# Last updated: 9/2/2025, 1:42:15 PM
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """Brute Force Solution1:
        fc=0
        rval=0
        cc=0
        for val in nums:
            for val2 in nums:
                if val==val2:
                    cc+=1
            if cc>fc:
                fc=cc
                rval=val
            cc=0
        return rval"""
        """Brute Force Solution:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j and nums[i]==nums[j]:
                    return nums[i]"""
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        return max(freq,key=freq.get)

        