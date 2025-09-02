# Last updated: 9/2/2025, 1:44:11 PM
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in range(len(s)):
            if s[i] in '([{':
                stack.append(s[i])
            else: 
                if not stack:
                    return False
                if s[i] is ')' and stack[-1] is not'(':
                    return False
                if s[i] is '}' and stack[-1] is not'{':
                    return False
                if s[i] is ']' and stack[-1] is not '[':
                    return False
                stack.pop()
        return not stack
        