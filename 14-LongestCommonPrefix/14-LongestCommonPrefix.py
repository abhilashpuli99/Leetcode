# Last updated: 9/2/2025, 1:44:15 PM
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        p=0
        q=0
        m=0
        n=len(strs)-1
        temp=min(len(strs[m]),len(strs[n]))
        prefix=""
        while(temp):
            if strs[m][p]==strs[n][q]:
                prefix+=strs[m][p]
                p+=1
                q+=1
                temp-=1
            elif strs[m][p]!=strs[n][q]:
                return prefix
        return prefix
        