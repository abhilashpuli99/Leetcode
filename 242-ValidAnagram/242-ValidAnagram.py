# Last updated: 9/2/2025, 1:42:22 PM
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s=list(s)
        t=list(t)
        if len(s)!=len(t):
            return False
        else:
            return sorted(s)==sorted(t)
        