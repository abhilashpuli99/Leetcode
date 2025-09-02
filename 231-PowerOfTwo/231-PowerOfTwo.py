# Last updated: 9/2/2025, 1:42:27 PM
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and (n&-n)==n