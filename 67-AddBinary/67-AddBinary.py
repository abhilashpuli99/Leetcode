# Last updated: 9/2/2025, 1:43:40 PM
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]
        