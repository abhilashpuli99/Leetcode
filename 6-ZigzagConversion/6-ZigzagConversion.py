# Last updated: 9/2/2025, 1:44:23 PM
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:  return s
        result=""
        for r in range(numRows):
            incr=2*(numRows-1)
            for indx in range(r,len(s),incr):
                result+=s[indx]
                if(r>0 and r<numRows-1 and indx+incr-2*r<len(s)):
                    result+=s[indx+incr-2*r]
        return result