# Last updated: 9/2/2025, 1:42:07 PM
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        pos=len(s)-1
        for i in range(len(s)//2):
            s[i],s[pos]=s[pos],s[i]
            pos-=1
        return s