# Last updated: 9/2/2025, 1:44:24 PM
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=""
        n=len(s)
        maxlen=0
        for i in range(n):
            l=r=i
            while l>=0 and r<n and s[l]==s[r]:
                if maxlen<(r-l+1):
                    maxlen=r-l+1
                    res=s[l:r+1]
                l-=1
                r+=1
            l=i
            r=i+1
            while l>=0 and r<n and s[l]==s[r]:
                if maxlen<(r-l+1):
                    maxlen=(r-l+1)
                    res=s[l:r+1]
                l-=1
                r+=1
        return res
        