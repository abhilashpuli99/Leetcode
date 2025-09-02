# Last updated: 9/2/2025, 1:43:13 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        while(left<right):
            if s[left].isalnum() and s[right].isalnum() and s[left].lower()!=s[right].lower():
                return False
            elif not s[left].isalnum():
                left+=1
            elif not s[right].isalnum():
                right-=1
            else:
                left+=1
                right-=1
        return True
        """Less Branching Best Optimal
        def isPalindrome(self, s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
"""
                
        