# Last updated: 9/2/2025, 1:44:05 PM
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if needle not in haystack:
            return -1
        return haystack.find(needle)
        