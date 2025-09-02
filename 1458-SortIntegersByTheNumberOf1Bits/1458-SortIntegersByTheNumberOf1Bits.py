# Last updated: 9/2/2025, 1:41:15 PM
class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))
    