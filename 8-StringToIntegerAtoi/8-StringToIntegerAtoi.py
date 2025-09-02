# Last updated: 9/2/2025, 1:44:20 PM
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        idx=0
        result=0
        sign=1
        n=len(s)
        if n==0:
            return 0
        while idx<n and s[idx]==' ':
            idx+=1
        if idx<n and (s[idx]=='+'or s[idx]=='-'):
            if s[idx]=='-':
                sign=-1
            idx+=1
        while idx<n and(s[idx]<='9' and s[idx]>='0'):
            result=result*10+(ord(s[idx])-ord('0'))
            if result>2**31-1:
                return sign*(2**31-1) if sign==1 else -2**31
            idx+=1
        return result*sign
