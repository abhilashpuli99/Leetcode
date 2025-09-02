# Last updated: 9/2/2025, 1:40:55 PM
class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        if len(words)!=len(s):
            return False
        for i in range(0,len(s)):
            if(words[i][0]!=s[i] or words[i]==0):
                return False
        return True
            