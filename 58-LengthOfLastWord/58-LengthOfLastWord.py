# Last updated: 9/2/2025, 1:43:44 PM
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        for word in s.split():
            length=len(word)
        return length