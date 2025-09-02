# Last updated: 9/2/2025, 1:42:50 PM
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber>0:
            columnNumber-=1
            result.append(chr(columnNumber%26+ord('A')))
            columnNumber//=26
        return "".join(result[::-1])