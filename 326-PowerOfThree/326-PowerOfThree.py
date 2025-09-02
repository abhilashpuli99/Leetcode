# Last updated: 9/2/2025, 1:42:10 PM
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n>0 and 3**19%n==0